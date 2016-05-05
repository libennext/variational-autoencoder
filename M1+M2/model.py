# -*- coding: utf-8 -*-
from args import args
from vae_m1 import BernoulliM1VAE, GaussianM1VAE, Conf as Conf1
from vae_m2 import BernoulliM2VAE, GaussianM2VAE, Conf as Conf2

# M1
conf1 = Conf1()
conf1.use_gpu = False if args.use_gpu == -1 else True
conf1.ndim_x = 28 * 28
conf1.ndim_z = 50
conf1.encoder_apply_batchnorm_to_input = True
conf1.encoder_apply_batchnorm = True
conf1.decoder_apply_batchnorm_to_input = True
conf1.decoder_apply_batchnorm = True
conf1.encoder_units = [600, 600]
conf1.decoder_units = [600, 600]
vae1 = BernoulliM1VAE(conf1, name="m1")

# M2
conf2 = Conf2()
conf2.use_gpu = False if args.use_gpu == -1 else True
conf2.ndim_x = 50
conf2.ndim_z = 50
conf2.encoder_xy_z_apply_batchnorm_to_input = True
conf2.encoder_x_y_apply_batchnorm_to_input = True
conf2.decoder_apply_batchnorm_to_input = True
conf2.encoder_x_y_apply_dropout = True
conf2.encoder_xy_z_apply_dropout = True
conf2.decoder_apply_dropout = True
conf2.encoder_xy_z_hidden_units = [500]
conf2.encoder_x_y_hidden_units = [500]
conf2.decoder_hidden_units = [500]
vae2 = GaussianM2VAE(conf2, name="m2")