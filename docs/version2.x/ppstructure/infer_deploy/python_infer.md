---
comments: true
---

# 基于Python预测引擎推理

## 1. 版面信息抽取

进入`ppstructure`目录

```bash linenums="1"
cd ppstructure
```

下载模型

```bash linenums="1"
mkdir inference && cd inference
# 下载PP-StructureV2版面分析模型并解压
wget https://paddleocr.bj.bcebos.com/ppstructure/models/layout/picodet_lcnet_x1_0_layout_infer.tar && tar xf picodet_lcnet_x1_0_layout_infer.tar
# 下载PP-OCRv3文本检测模型并解压
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/PP-OCRv3_mobile_det_infer.tar && tar xf PP-OCRv3_mobile_det_infer.tar
# 下载PP-OCRv3文本识别模型并解压
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/PP-OCRv3_mobile_rec_infer.tar && tar xf PP-OCRv3_mobile_rec_infer.tar
# 下载PP-StructureV2表格识别模型并解压
wget https://paddleocr.bj.bcebos.com/ppstructure/models/slanet/paddle3.0b2/ch_ppstructure_mobile_v2.0_SLANet_infer.tar && tar xf ch_ppstructure_mobile_v2.0_SLANet_infer.tar
cd ..
```

### 1.1 版面分析+表格识别

```bash linenums="1"
python3 predict_system.py --det_model_dir=inference/PP-OCRv3_mobile_det_infer \
                          --rec_model_dir=inference/PP-OCRv3_mobile_rec_infer \
                          --table_model_dir=inference/ch_ppstructure_mobile_v2.0_SLANet_infer \
                          --layout_model_dir=inference/picodet_lcnet_x1_0_layout_infer \
                          --image_dir=./docs/table/1.png \
                          --rec_char_dict_path=../ppocr/utils/ppocr_keys_v1.txt \
                          --table_char_dict_path=../ppocr/utils/dict/table_structure_dict_ch.txt \
                          --output=../output \
                          --vis_font_path=../doc/fonts/simfang.ttf
```

运行完成后，每张图片会在`output`字段指定的目录下的`structure`目录下有一个同名目录，图片里的每个表格会存储为一个excel，图片区域会被裁剪之后保存下来，excel文件和图片名为表格在图片里的坐标。详细的结果会存储在`res.txt`文件中。

### 1.2 版面分析

```bash linenums="1"
python3 predict_system.py --layout_model_dir=inference/picodet_lcnet_x1_0_layout_infer \
                          --image_dir=./docs/table/1.png \
                          --output=../output \
                          --table=false \
                          --ocr=false
```

运行完成后，每张图片会在`output`字段指定的目录下的`structure`目录下有一个同名目录，图片区域会被裁剪之后保存下来，图片名为表格在图片里的坐标。版面分析结果会存储在`res.txt`文件中。

### 1.3 表格识别

```bash linenums="1"
python3 predict_system.py --det_model_dir=inference/PP-OCRv3_mobile_det_infer \
                          --rec_model_dir=inference/PP-OCRv3_mobile_rec_infer \
                          --table_model_dir=inference/ch_ppstructure_mobile_v2.0_SLANet_infer \
                          --image_dir=./docs/table/table.jpg \
                          --rec_char_dict_path=../ppocr/utils/ppocr_keys_v1.txt \
                          --table_char_dict_path=../ppocr/utils/dict/table_structure_dict_ch.txt \
                          --output=../output \
                          --vis_font_path=../doc/fonts/simfang.ttf \
                          --layout=false
```

运行完成后，每张图片会在`output`字段指定的目录下的`structure`目录下有一个同名目录，表格会存储为一个excel，excel文件名为`[0,0,img_h,img_w]`。

## 2. 关键信息抽取

### 2.1 SER

```bash linenums="1"
cd ppstructure

mkdir inference && cd inference
# 下载SER XFUND 模型并解压
wget https://paddleocr.bj.bcebos.com/ppstructure/models/vi_layoutxlm/ser_vi_layoutxlm_xfund_infer.tar && tar -xf ser_vi_layoutxlm_xfund_infer.tar
cd ..
python3 predict_system.py \
  --kie_algorithm=LayoutXLM \
  --ser_model_dir=./inference/ser_vi_layoutxlm_xfund_infer \
  --image_dir=./docs/kie/input/zh_val_42.jpg \
  --ser_dict_path=../ppocr/utils/dict/kie_dict/xfund_class_list.txt \
  --vis_font_path=../doc/fonts/simfang.ttf \
  --ocr_order_method="tb-yx" \
  --mode=kie
```

运行完成后，每张图片会在`output`字段指定的目录下的`kie`目录下存放可视化之后的图片，图片名和输入图片名一致。

### 2.2 RE+SER

```bash linenums="1"
cd ppstructure

mkdir inference && cd inference
# 下载RE SER XFUND 模型并解压
wget https://paddleocr.bj.bcebos.com/ppstructure/models/vi_layoutxlm/ser_vi_layoutxlm_xfund_infer.tar && tar -xf ser_vi_layoutxlm_xfund_infer.tar
wget https://paddleocr.bj.bcebos.com/ppstructure/models/vi_layoutxlm/re_vi_layoutxlm_xfund_infer.tar && tar -xf re_vi_layoutxlm_xfund_infer.tar
cd ..

python3 predict_system.py \
  --kie_algorithm=LayoutXLM \
  --re_model_dir=./inference/re_vi_layoutxlm_xfund_infer \
  --ser_model_dir=./inference/ser_vi_layoutxlm_xfund_infer \
  --image_dir=./docs/kie/input/zh_val_42.jpg \
  --ser_dict_path=../ppocr/utils/dict/kie_dict/xfund_class_list.txt \
  --vis_font_path=../doc/fonts/simfang.ttf \
  --ocr_order_method="tb-yx" \
  --mode=kie
```

运行完成后，每张图片会在`output`字段指定的目录下的`kie`目录下有一个同名目录，目录中存放可视化图片和预测结果。
