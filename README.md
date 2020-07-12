

# Monocular Depth Estimation and Segmentation Dataset

Create a custom dataset for monocular depth estimation and segmentation simultaneously. Since we do not have access to a depth camera, we use a pre-trained depth model to generate the depth maps which will be used as the ground truth for our model.

### Dataset Samples
Background:

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

Foreground:

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

Foreground Mask:

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

Foreground-Background:

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

Foreground-Background Mask:


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


Foreground-Background Depth:


