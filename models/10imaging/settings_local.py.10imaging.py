# Define critical settings and/or override defaults specified in
# settings.py. Copy this file to settings_local.py in the same
# directory as settings.py and edit. Any settings defined here
# will override those defined in settings.py



# Set this to point to your compiled checkout of caffe
caffevis_caffe_root      = '/Users/ten/10imaging/caffe'

# Load model: bvlc-googlenet
# Path to caffe deploy prototxt file. Minibatch size should be 1.
caffevis_deploy_prototxt = '%DVT_ROOT%/models/10imaging/deploy_23.prototxt'

# Path to network weights to load.
caffevis_network_weights = '%DVT_ROOT%/models/10imaging/caffenet_23.caffemodel'

# Other optional settings; see complete documentation for each in settings.py.
caffevis_data_mean       = (104, 117, 123)   # per-channel mean
caffevis_labels          = '%DVT_ROOT%/models/10imaging/labels.txt'
caffevis_jpgvis_layers   = []
caffevis_label_layers    = ('fc8', 'prob')
caffevis_prob_layer      = 'prob'
def caffevis_layer_pretty_name_fn(name):
    return name.replace('pool','p').replace('norm','n')

_control_height = 125
window_panes = (
    # (i, j, i_size, j_size)
    ('input',            (  0,    0,  300,   300)),
    ('caffevis_aux',     (300,    0,  300,   300)),
    ('caffevis_back',    (600,    0,  300,   300)),
    ('caffevis_status',  (900,    0,   30,  1500)),
    ('caffevis_control', (  0,  300,   _control_height, 1200)),
    ('caffevis_layers',  ( _control_height,  300,  900 - _control_height, 1200)),
)
# Use GPU? Default is True.
caffevis_mode_gpu = False
# Display tweaks.
# Scale all window panes in UI by this factor
#global_scale = 1.0
# Scale all fonts by this factor    
#global_font_size = 1.0

