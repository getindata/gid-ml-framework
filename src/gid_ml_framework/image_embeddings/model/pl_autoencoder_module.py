from torch import optim, nn
import pytorch_lightning as pl
import mlflow
import matplotlib.pyplot as plt
import numpy as np
from kedro_mlflow.config import kedro_mlflow_config

# it's needed, so matplotlib artifacts are saved together with the mlflow run
mlflow.set_experiment(experiment_name=kedro_mlflow_config.get_mlflow_config().tracking.experiment.name)


class LitAutoEncoder(pl.LightningModule):
    def __init__(self, encoder, decoder):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, x):
        embedding = self.encoder(x)
        return embedding

    def training_step(self, batch, batch_idx):
        x, _ = batch
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = nn.functional.mse_loss(x_hat.flatten(), x.flatten())
        self.log("train_loss", loss, on_epoch=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, _ = batch
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = nn.functional.mse_loss(x_hat.flatten(), x.flatten())
        self.log("val_loss", loss, on_epoch=True)
        return {'val_loss': loss,
                'x_hat': x_hat,
                'x': x}

    def configure_optimizers(self):
        optimizer = optim.Adam(self.parameters(), lr=1e-3)
        return optimizer

    def predict_step(self, batch, batch_idx, dataloader_idx=0):
        x, y = batch
        embedding = self.encoder(x)
        return embedding, y

    def validation_epoch_end(self, outputs, no_plot_images=8):
        results = outputs[0]
        self._save_reconstructed_plots(results, self.current_epoch, no_plot_images)

    @staticmethod
    def _save_reconstructed_plots(results, current_epoch, no_plot_images=8):
        fig, axarr = plt.subplots(no_plot_images, 2, figsize=(8, no_plot_images*1.5))
        for i in range(no_plot_images):
            img_reconstructed = results['x_hat'][i, :].reshape(3, 128, 128)
            img_original = results['x'][i, :].reshape(3, 128, 128)
            axarr[i, 0].imshow(np.transpose(img_reconstructed.numpy(), (1, 2, 0)))
            axarr[i, 1].imshow(np.transpose(img_original.numpy(), (1, 2, 0)))
        mlflow.log_figure(plt.gcf(), f'reconstructed/img_reconstructed_{current_epoch}.png')
        plt.close()
