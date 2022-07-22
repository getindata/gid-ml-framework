import pytorch_lightning as pl
from gid_ml_framework.image_embeddings.data.hm_data import HMDataLoader
from gid_ml_framework.image_embeddings.model.pl_autoencoder_module import LitAutoEncoder
from gid_ml_framework.image_embeddings.model import pl_encoders, pl_decoders
import mlflow.pytorch
from pytorch_lightning.utilities.seed import seed_everything
from typing import List


def train_image_embeddings(
    img_dir: str,
    encoder: str,
    decoder: str,
    batch_size: int = 32,
    image_size: List[int] = [128, 128],
    embedding_size: int = 32,
    num_epochs: int = 5,
    shuffle_reconstructions: bool = False,
    save_model: bool = False,
    model_name: str = "image_embeddings_model",
    seed: int = 321) -> None:

    seed_everything(seed, True)

    hm_dataloader = HMDataLoader(img_dir, batch_size=batch_size)
    hm_encoder = getattr(pl_encoders, encoder)
    hm_decoder = getattr(pl_decoders, decoder)

    hm_autoencoder = LitAutoEncoder(
        encoder=hm_encoder(embedding_size, image_size),
        decoder=hm_decoder(embedding_size, image_size),
        shuffle_reconstructions=shuffle_reconstructions
        )
    
    early_stop_callback = pl.callbacks.early_stopping.EarlyStopping(
        monitor='val_loss',
        min_delta=0.00001,
        patience=5,
        verbose=True,
        mode='min'
    )

    hm_trainer = pl.Trainer(limit_train_batches=100,
        max_epochs=num_epochs, 
        logger=False, # disabling pytorch_lightning default logging, because we have mlflow
        enable_checkpointing=False,
        callbacks=[early_stop_callback])

    mlflow.pytorch.autolog(log_models=save_model, registered_model_name=model_name)

    hm_trainer.fit(model=hm_autoencoder, train_dataloaders=hm_dataloader)
