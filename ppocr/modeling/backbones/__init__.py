# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = ["build_backbone"]


def build_backbone(config, model_type):
    if model_type == "det" or model_type == "table":
        from .det_mobilenet_v3 import MobileNetV3
        from .det_resnet import ResNet
        from .det_resnet_vd import ResNet_vd
        from .det_resnet_vd_sast import ResNet_SAST
        from .det_pp_lcnet import PPLCNet
        from .rec_lcnetv3 import PPLCNetV3
        from .rec_hgnet import PPHGNet_small
        from .rec_vit import ViT
        from .det_pp_lcnet_v2 import PPLCNetV2_base
        from .rec_repvit import RepSVTR_det
        from .rec_vary_vit import Vary_VIT_B
        from .rec_pphgnetv2 import PPHGNetV2_B4

        support_dict = [
            "MobileNetV3",
            "ResNet",
            "ResNet_vd",
            "ResNet_SAST",
            "PPLCNet",
            "PPLCNetV3",
            "PPHGNet_small",
            "PPLCNetV2_base",
            "RepSVTR_det",
            "Vary_VIT_B",
            "PPHGNetV2_B4",
        ]
        if model_type == "table":
            from .table_master_resnet import TableResNetExtra

            support_dict.append("TableResNetExtra")
    elif model_type == "rec" or model_type == "cls":
        from .rec_mobilenet_v3 import MobileNetV3
        from .rec_resnet_vd import ResNet
        from .rec_resnet_fpn import ResNetFPN
        from .rec_mv1_enhance import MobileNetV1Enhance
        from .rec_nrtr_mtb import MTB
        from .rec_resnet_31 import ResNet31
        from .rec_resnet_32 import ResNet32
        from .rec_resnet_45 import ResNet45
        from .rec_resnet_aster import ResNet_ASTER
        from .rec_micronet import MicroNet
        from .rec_efficientb3_pren import EfficientNetb3_PREN
        from .rec_svtrnet import SVTRNet
        from .rec_vitstr import ViTSTR
        from .rec_resnet_rfl import ResNetRFL
        from .rec_densenet import DenseNet
        from .rec_resnetv2 import ResNetV2
        from .rec_hybridvit import HybridTransformer
        from .rec_donut_swin import DonutSwinModel
        from .rec_shallow_cnn import ShallowCNN
        from .rec_lcnetv3 import PPLCNetV3
        from .rec_hgnet import PPHGNet_small
        from .rec_vit_parseq import ViTParseQ
        from .rec_repvit import RepSVTR
        from .rec_svtrv2 import SVTRv2
        from .rec_vary_vit import Vary_VIT_B, Vary_VIT_B_Formula
        from .rec_pphgnetv2 import (
            PPHGNetV2_B4,
            PPHGNetV2_B4_Formula,
            PPHGNetV2_B6_Formula,
        )

        support_dict = [
            "MobileNetV1Enhance",
            "MobileNetV3",
            "ResNet",
            "ResNetFPN",
            "MTB",
            "ResNet31",
            "ResNet45",
            "ResNet_ASTER",
            "MicroNet",
            "EfficientNetb3_PREN",
            "SVTRNet",
            "ViTSTR",
            "ResNet32",
            "ResNetRFL",
            "DenseNet",
            "ShallowCNN",
            "PPLCNetV3",
            "PPHGNet_small",
            "ViTParseQ",
            "ViT",
            "RepSVTR",
            "SVTRv2",
            "ResNetV2",
            "HybridTransformer",
            "DonutSwinModel",
            "Vary_VIT_B",
            "PPHGNetV2_B4",
            "PPHGNetV2_B4_Formula",
            "PPHGNetV2_B6_Formula",
            "Vary_VIT_B_Formula",
        ]
    elif model_type == "e2e":
        from .e2e_resnet_vd_pg import ResNet

        support_dict = ["ResNet"]
    elif model_type == "kie":
        from .kie_unet_sdmgr import Kie_backbone
        from .vqa_layoutlm import (
            LayoutLMForSer,
            LayoutLMv2ForSer,
            LayoutLMv2ForRe,
            LayoutXLMForSer,
            LayoutXLMForRe,
        )

        support_dict = [
            "Kie_backbone",
            "LayoutLMForSer",
            "LayoutLMv2ForSer",
            "LayoutLMv2ForRe",
            "LayoutXLMForSer",
            "LayoutXLMForRe",
        ]
    elif model_type == "table":
        from .table_resnet_vd import ResNet
        from .table_mobilenet_v3 import MobileNetV3
        from .rec_vary_vit import Vary_VIT_B

        support_dict = ["ResNet", "MobileNetV3", "Vary_VIT_B"]
    else:
        raise NotImplementedError

    module_name = config.pop("name")
    assert module_name in support_dict, Exception(
        "when model typs is {}, backbone only support {}".format(
            model_type, support_dict
        )
    )
    module_class = eval(module_name)(**config)
    return module_class
