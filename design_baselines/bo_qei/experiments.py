from ray import tune
import click
import ray
import os


@click.group()
def cli():
    """A group of experiments for training Conservative Score Models
    and reproducing our ICLR 2021 results.
    """


#############


@cli.command()
@click.option('--local-dir', type=str, default='bo-qei-dkitty')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def dkitty(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate BO-QEI on DKittyMorphology-Exact-v0
    """

    # Final Version

    from design_baselines.bo_qei import bo_qei
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(bo_qei, config={
        "logging_dir": "data",
        "normalize_ys": True,
        "normalize_xs": True,
        "task": "DKittyMorphology-Exact-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "embedding_size": 256,
        "hidden_size": 256,
        "num_layers": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "bo_noise_se": 0.1,
        "bo_gp_samples": 500,
        "bo_batch_size": 32,
        "bo_num_restarts": 10,
        "bo_raw_samples": 128,
        "bo_batch_limit": 5,
        "bo_maxiter": 200,
        "bo_iterations": 20,
        "bo_mc_samples": 128,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='bo-qei-ant')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def ant(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate BO-QEI on AntMorphology-Exact-v0
    """

    # Final Version

    from design_baselines.bo_qei import bo_qei
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(bo_qei, config={
        "logging_dir": "data",
        "normalize_ys": True,
        "normalize_xs": True,
        "task": "AntMorphology-Exact-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "embedding_size": 256,
        "hidden_size": 256,
        "num_layers": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "bo_noise_se": 0.1,
        "bo_gp_samples": 500,
        "bo_batch_size": 32,
        "bo_num_restarts": 10,
        "bo_raw_samples": 128,
        "bo_batch_limit": 5,
        "bo_maxiter": 200,
        "bo_iterations": 20,
        "bo_mc_samples": 128,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='bo-qei-hopper')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def hopper(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate BO-QEI on HopperController-Exact-v0
    """

    # Final Version

    from design_baselines.bo_qei import bo_qei
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(bo_qei, config={
        "logging_dir": "data",
        "normalize_ys": True,
        "normalize_xs": True,
        "task": "HopperController-Exact-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "embedding_size": 256,
        "hidden_size": 256,
        "num_layers": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "bo_noise_se": 0.1,
        "bo_gp_samples": 500,
        "bo_batch_size": 32,
        "bo_num_restarts": 10,
        "bo_raw_samples": 128,
        "bo_batch_limit": 5,
        "bo_maxiter": 200,
        "bo_iterations": 20,
        "bo_mc_samples": 128,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='bo-qei-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def superconductor(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate BO-QEI on Superconductor-FullyConnected-v0
    """

    # Final Version

    from design_baselines.bo_qei import bo_qei
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(bo_qei, config={
        "logging_dir": "data",
        "normalize_ys": True,
        "normalize_xs": True,
        "task": "Superconductor-FullyConnected-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "embedding_size": 256,
        "hidden_size": 256,
        "num_layers": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "bo_noise_se": 0.1,
        "bo_gp_samples": 500,
        "bo_batch_size": 32,
        "bo_num_restarts": 10,
        "bo_raw_samples": 128,
        "bo_batch_limit": 5,
        "bo_maxiter": 200,
        "bo_iterations": 20,
        "bo_mc_samples": 128,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='bo-qei-chembl')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def chembl(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate BO-QEI on ChEMBL-ResNet-v0
    """

    # Final Version

    from design_baselines.bo_qei import bo_qei
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(bo_qei, config={
        "logging_dir": "data",
        "normalize_ys": True,
        "normalize_xs": True,
        "task": "ChEMBL-ResNet-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "embedding_size": 256,
        "hidden_size": 256,
        "num_layers": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "bo_noise_se": 0.1,
        "bo_gp_samples": 500,
        "bo_batch_size": 32,
        "bo_num_restarts": 10,
        "bo_raw_samples": 128,
        "bo_batch_limit": 5,
        "bo_maxiter": 200,
        "bo_iterations": 20,
        "bo_mc_samples": 128,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='bo-qei-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def gfp(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate BO-QEI on GFP-Transformer-v0
    """

    # Final Version

    from design_baselines.bo_qei import bo_qei
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(bo_qei, config={
        "logging_dir": "data",
        "normalize_ys": True,
        "normalize_xs": True,
        "task": "GFP-Transformer-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "embedding_size": 256,
        "hidden_size": 256,
        "num_layers": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "bo_noise_se": 0.1,
        "bo_gp_samples": 500,
        "bo_batch_size": 32,
        "bo_num_restarts": 10,
        "bo_raw_samples": 128,
        "bo_batch_limit": 5,
        "bo_maxiter": 200,
        "bo_iterations": 20,
        "bo_mc_samples": 128,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='bo-qei-tf-bind-8')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def tf_bind_8(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate BO-QEI on TFBind8-Exact-v0
    """

    # Final Version

    from design_baselines.bo_qei import bo_qei
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(bo_qei, config={
        "logging_dir": "data",
        "normalize_ys": True,
        "normalize_xs": True,
        "task": "TFBind8-Exact-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "embedding_size": 256,
        "hidden_size": 256,
        "num_layers": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "bo_noise_se": 0.1,
        "bo_gp_samples": 500,
        "bo_batch_size": 32,
        "bo_num_restarts": 10,
        "bo_raw_samples": 128,
        "bo_batch_limit": 5,
        "bo_maxiter": 200,
        "bo_iterations": 20,
        "bo_mc_samples": 128,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='bo-qei-utr')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def utr(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate BO-QEI on UTR-Transformer-v0
    """

    # Final Version

    from design_baselines.bo_qei import bo_qei
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(bo_qei, config={
        "logging_dir": "data",
        "normalize_ys": True,
        "normalize_xs": True,
        "task": "UTR-Transformer-v0",
        "task_kwargs": {},
        "bootstraps": 5,
        "val_size": 200,
        "ensemble_batch_size": 100,
        "embedding_size": 256,
        "hidden_size": 256,
        "num_layers": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "ensemble_lr": 0.001,
        "ensemble_epochs": 100,
        "bo_noise_se": 0.1,
        "bo_gp_samples": 500,
        "bo_batch_size": 32,
        "bo_num_restarts": 10,
        "bo_raw_samples": 128,
        "bo_batch_limit": 5,
        "bo_maxiter": 200,
        "bo_iterations": 20,
        "bo_mc_samples": 128,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})
