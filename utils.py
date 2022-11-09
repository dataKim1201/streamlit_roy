import albumentations
import albumentations.pytorch
import torch

import io
from IPython.display import Image as display_image
from PIL import Image
import numpy as np
def transform_image(image_bytes) -> torch.Tensor:
    transform = albumentations.Compose([
            albumentations.Resize(height=512, width=384),
            albumentations.Normalize(mean=(0.5, 0.5, 0.5), 
                                     std=(0.2, 0.2, 0.2)),
            albumentations.pytorch.transforms.ToTensorV2()
        ])
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert('RGB')
    image_array = np.array(image)
    return transform(image=image_array)['image'].unsqueeze(0)



# def on_display_click_callback(clicked_button : widgets.Button)->None:
#     global content
#     uploaded_filename = next(iter(uploader.value))
#     content = uploader.value[uploaded_filename]['content']
#     display_image_space.value = content
# def on_inference_click_callback(click_button : widgets.Button) -> None:
#     with inference_output:
#         inference_output.clear_output()
#         _, output  = get_prediction(content)
#         print(config['classes'][output.item()])