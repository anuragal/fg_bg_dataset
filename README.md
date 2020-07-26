

# Monocular Depth Estimation and Segmentation Dataset

Create a custom dataset for monocular depth estimation and segmentation simultaneously. Since we do not have access to a depth camera, we use a pre-trained depth model to generate the depth maps which will be used as the ground truth for our model.

### Dataset Samples

#### Background (bg)
 - 99 Images of places like restaurent, malls or home.
 - Each image was resized to 224 x 224. Final Image dimensions: (224, 224, 3). Total size: 1.5M
 - Mean: [0.5442, 0.5057, 0.4621]
 - Std: [0.2609, 0.2624, 0.2799]

<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bg/bg_001.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bg/bg_002.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bg/bg_003.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bg/bg_011.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bg/bg_005.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bg/bg_006.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bg/bg_007.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bg/bg_008.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bg/bg_009.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bg/bg_010.jpg" height="8%" width="8%" ></a>

#### Foreground (fg)
 - 99 Images of humans & very few animals with transparent background.
 - Images were rescaled to keep height 140 and resizing width while maintaining aspect ratio. [Code](https://github.com/anuragal/fg_bg_dataset/blob/master/utils/image_resize.py) to resize images
 - Image dimensions: (140, width, 4)
 - Directory size: 1.8M

<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg/fg_001.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg/fg_002.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg/fg_003.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg/fg_011.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg/fg_005.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg/fg_006.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg/fg_007.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg/fg_008.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg/fg_009.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg/fg_010.png" height="8%" width="8%" ></a>

#### Foreground Mask (fg_mask)
 - For every foreground, corresponding mask image was created
 - Wrote custom [code](https://github.com/anuragal/fg_bg_dataset/blob/master/utils/mask.py) to generate foreground mask
 - Image dimensions: (140, width)
 - Directory size: 848k
 
 <a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg_mask/mask_fg_001.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg_mask/mask_fg_002.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg_mask/mask_fg_003.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg_mask/mask_fg_011.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg_mask/mask_fg_005.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg_mask/mask_fg_006.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg_mask/mask_fg_007.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg_mask/mask_fg_008.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg_mask/mask_fg_009.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/fg_mask/mask_fg_010.png" height="8%" width="8%" ></a>

#### Foreground Overlayed on Background (bgfg)
 - For each background
	 - Overlay each foreground randomly 20 times on the background
	 - Flip the foreground and again overlay it randomly 20 times on the background
  - [Code](https://github.com/anuragal/fg_bg_dataset/blob/master/utils/overlay.py) to generate overlay images
 - Number of images: 99 * 99 * 2 * 20 = 3,92,040
 - Image dimensions: (224, 224, 3)
 - Directory size: 5.3G
 - Mean: [0.5365, 0.4978, 0.4601]
 - Std: [0.2671, 0.2650, 0.2799]

<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_overlay/ol_bg001fg0011_fg_001.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_overlay/ol_bg002fg0021_fg_002.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_overlay/ol_bg003fg0031_fg_003.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_overlay/ol_bg011fg0111_fg_011.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_overlay/ol_bg005fg0051_fg_005.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_overlay/ol_bg006fg0061_fg_006.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_overlay/ol_bg007fg0071_fg_007.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_overlay/ol_bg008fg0081_fg_008.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_overlay/ol_bg009fg0091_fg_009.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_overlay/ol_bg010fg0101_fg_010.png" height="8%" width="8%" ></a>

#### Foreground Overlayed on Background Mask (bgfg_mask)
 - For every overlayed image, corresponding mask image was created
 - Wrote custom [code](https://github.com/anuragal/fg_bg_dataset/blob/master/utils/mask.py) to generate mask
 - Number of images: 3,92,041
 - Image dimensions: (224, 224)
 - Directory size: 1.6G
 - Mean: [0.0943]
 - Std: [0.2856]

<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_mask/mask_ol_bg001fg0011_fg_001.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_mask/mask_ol_bg002fg0021_fg_002.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_mask/mask_ol_bg003fg0031_fg_003.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_mask/mask_ol_bg011fg0111_fg_011.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_mask/mask_ol_bg005fg0051_fg_005.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_mask/mask_ol_bg006fg0061_fg_006.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_mask/mask_ol_bg007fg0071_fg_007.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_mask/mask_ol_bg008fg0081_fg_008.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_mask/mask_ol_bg009fg0091_fg_009.png" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_mask/mask_ol_bg010fg0101_fg_010.png" height="8%" width="8%" ></a>


#### Foreground Overlayed on Background Depth Map (bgfg_depth)
 - Depth map was generated for every overlay image.
 - A pre-trained monocular depth estimation model [DenseDepth](https://github.com/anuragal/DepthModel/blob/master/DenseDepth.ipynb) was used to generate the depth maps.
 - Image was stored as a grayscale image.
 - Number of images: 3,92,041
 - Image dimensions: (224, 224)
 - Directory size: 1.6G
 - Mean: [0.4334]
 - Std: [0.2715]


<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_depth/depth_ol_bg001fg0011_fg_001.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_depth/depth_ol_bg002fg0021_fg_002.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_depth/depth_ol_bg003fg0031_fg_003.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_depth/depth_ol_bg011fg0111_fg_011.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_depth/depth_ol_bg005fg0051_fg_005.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_depth/depth_ol_bg006fg0061_fg_006.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_depth/depth_ol_bg007fg0071_fg_007.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_depth/depth_ol_bg008fg0081_fg_008.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_depth/depth_ol_bg009fg0091_fg_009.jpg" height="8%" width="8%" ></a>
<a href="url"><img src="https://github.com/anuragal/fg_bg_dataset/blob/master/bgfg_depth/depth_ol_bg010fg0101_fg_010.jpg" height="8%" width="8%" ></a>


### Image dimensions

Image dimensions are generated using [code](https://github.com/anuragal/DepthModel/blob/master/generate_data_stats.ipynb) 
