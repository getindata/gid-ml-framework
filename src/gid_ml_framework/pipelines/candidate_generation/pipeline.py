from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import (
    collect_global_articles, assign_global_articles,
    segment_by_customer_age, collect_segment_articles, assign_segment_articles,
    collect_previously_bought_articles, collect_previously_bought_prod_name_articles,
    collect_similar_embeddings,
    collect_all_candidates
)


def create_pipeline(**kwargs) -> Pipeline:
    global_pipeline = pipeline(
        [
            node(
                func=collect_global_articles,
                inputs=[
                    # transactions
                    "train_transactions",
                    "params:candidate_generation.global_articles.n_days",
                    "params:candidate_generation.global_articles.top_n",
                    ],
                outputs="global_articles_set",
                name="collect_global_articles_node",
            ),
            node(
                func=assign_global_articles,
                inputs=[
                    "customers_sample",
                    "global_articles_set",
                    ],
                outputs="global_articles_df",
                name="assign_global_articles_node",
            ),
        ],
        namespace="global_candidate_generation",
        # transactions
        inputs=["train_transactions", "customers_sample"],
        outputs=["global_articles_df"],
    )

    segment_pipeline = pipeline(
        [    
            node(
                func=segment_by_customer_age,
                inputs=[
                    "customers_sample",
                    "params:candidate_generation.segment_articles.no_segments",
                    ],
                outputs="customers_bins",
                name="segment_by_customer_age_node",
            ),
            node(
                func=collect_segment_articles,
                inputs=[
                    # transactions
                    "train_transactions",
                    "customers_bins",
                    "params:candidate_generation.segment_articles.n_days",
                    "params:candidate_generation.segment_articles.top_n",
                    ],
                outputs="segment_articles_dict",
                name="collect_segment_articles_node",
            ),
            node(
                func=assign_segment_articles,
                inputs=[
                    "segment_articles_dict",
                    "customers_bins",
                    ],
                outputs="segment_articles_df",
                name="assign_segment_articles_node",
            ),
        ],
        namespace="segment_candidate_generation",
        # transactions
        inputs=["train_transactions", "customers_sample"],
        outputs=["segment_articles_df"],
    )

    previously_bought_pipeline = pipeline(
        [    
            node(
                func=collect_previously_bought_articles,
                inputs=[
                    # transactions
                    "train_transactions",
                    ],
                outputs="prev_bought_df",
                name="collect_prev_bought_node",
            ),
            node(
                func=collect_previously_bought_prod_name_articles,
                inputs=[
                    # transactions
                    "train_transactions",
                    "articles_sample",
                    ],
                outputs="prev_bought_prod_name_df",
                name="collect_prev_bought_prod_name_node",
            ),
        ],
        namespace="prev_bought_candidate_generation",
        # transactions
        inputs=["train_transactions", "articles_sample"],
        outputs=["prev_bought_df", "prev_bought_prod_name_df"],
    )

    closest_image_embeddings_pipeline = pipeline(
        [    
            node(
                func=collect_similar_embeddings,
                inputs=[
                    # transactions
                    "train_transactions",
                    "image_embeddings",
                    "params:candidate_generation.image_embeddings.n_last_bought",
                    "params:candidate_generation.image_embeddings.k_closest",
                    "params:candidate_generation.image_embeddings.name",
                    ],
                outputs="closest_image_embeddings_df",
                name="closest_image_embeddings_node",
            ),
        ],
        namespace="closest_image_embeddings_candidate_generation",
        # transactions
        inputs=["train_transactions", "image_embeddings"],
        outputs=["closest_image_embeddings_df"],
    )

    closest_text_embeddings_pipeline = pipeline(
        [    
            node(
                func=collect_similar_embeddings,
                inputs=[
                    # transactions
                    "train_transactions",
                    "text_embeddings",
                    "params:candidate_generation.text_embeddings.n_last_bought",
                    "params:candidate_generation.text_embeddings.k_closest",
                    "params:candidate_generation.text_embeddings.name",
                    ],
                outputs="closest_text_embeddings_df",
                name="closest_text_embeddings_node",
            ),
        ],
        namespace="closest_text_embeddings_candidate_generation",
        # transactions
        inputs=["train_transactions", "text_embeddings"],
        outputs=["closest_text_embeddings_df"],
    )

    collect_candidates_pipeline = pipeline(
        [    
            node(
                func=collect_all_candidates,
                inputs=[
                    "global_articles_df",
                    "segment_articles_df",
                    "prev_bought_df",
                    "prev_bought_prod_name_df",
                    "closest_image_embeddings_df",
                    "closest_text_embeddings_df",
                    ],
                outputs="train_candidates",
                # candidates
                name="collect_all_candidates_node",
            ),
        ],
        namespace="collect_all_candidates",
        inputs=[
            "global_articles_df",
            "segment_articles_df",
            "prev_bought_df",
            "prev_bought_prod_name_df",
            "closest_image_embeddings_df",
            "closest_text_embeddings_df",
            ],
        outputs=["train_candidates"],
        # candidates
    )

    return (
        global_pipeline + 
        segment_pipeline + 
        previously_bought_pipeline + 
        closest_image_embeddings_pipeline +
        closest_text_embeddings_pipeline +
        collect_candidates_pipeline
        )
