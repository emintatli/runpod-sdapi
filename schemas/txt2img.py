TXT2IMG_SCHEMA = {
    'enable_hr': {
        'type': bool,
        'required': False,
        'default': False
    },
    'denoising_strength': {
        'type': float,
        'required': False,
        'default': 0
    },
    'firstphase_width': {
        'type': int,
        'required': False,
        'default': 0
    },
    'firstphase_height': {
        'type': int,
        'required': False,
        'default': 0
    },
    'hr_scale': {
        'type': int,
        'required': False,
        'default': 2
    },
    'hr_upscaler': {
        'type': str,
        'required': False,
        'default': ''
    },
    'hr_second_pass_steps': {
        'type': int,
        'required': False,
        'default': 0
    },
    'hr_resize_x': {
        'type': int,
        'required': False,
        'default': 0
    },
    'hr_resize_y': {
        'type': int,
        'required': False,
        'default': 0
    },
    'hr_sampler_name': {
        'type': str,
        'required': False,
        'default': ''
    },
    'hr_prompt': {
        'type': str,
        'required': False,
        'default': ''
    },
    'hr_negative_prompt': {
        'type': str,
        'required': False,
        'default': ''
    },
    'prompt': {
        'type': str,
        'required': True
    },
    'styles': {
        'type': list,
        'required': False,
        'default': []
    },
    'seed': {
        'type': int,
        'required': False,
        'default': -1
    },
    'subseed': {
        'type': int,
        'required': False,
        'default': -1
    },
    'subseed_strength': {
        'type': int,
        'required': False,
        'default': 0
    },
    'seed_resize_from_h': {
        'type': int,
        'required': False,
        'default': -1
    },
    'seed_resize_from_w': {
        'type': int,
        'required': False,
        'default': -1
    },
    'sampler_name': {
        'type': str,
        'required': False,
        'default': 'Euler a',
        'constraints': lambda sampler_name: sampler_name in [
            'Euler a',
            'Euler',
            'LMS',
            'Heun',
            'DPM2',
            'DPM2 a',
            'DPM++ 2S a',
            'DPM++ 2M',
            'DPM++ SDE',
            'DPM++ 2M SDE',
            'DPM fast',
            'DPM adaptive',
            'LMS Karras',
            'DPM2 Karras',
            'DPM2 a Karras',
            'DPM++ 2S a Karras',
            'DPM++ 2M Karras',
            'DPM++ SDE Karras',
            'DPM++ 2M SDE Karras',
            'DDIM',
            'PLMS',
            'UniPC'
        ]
    },
    'batch_size': {
        'type': int,
        'required': False,
        'default': 1
    },
    'n_iter': {
        'type': int,
        'required': False,
        'default': 1
    },
    'steps': {
        'type': int,
        'required': False,
        'default': 20
    },
    'cfg_scale': {
        'type': float,
        'required': False,
        'default': 7
    },
    'width': {
        'type': int,
        'required': False,
        'default': 512
    },
    'height': {
        'type': int,
        'required': False,
        'default': 512
    },
    'restore_faces': {
        'type': bool,
        'required': False,
        'default': False
    },
    'tiling': {
        'type': bool,
        'required': False,
        'default': False
    },
    'do_not_save_samples': {
        'type': bool,
        'required': False,
        'default': False
    },
    'do_not_save_grid': {
        'type': bool,
        'required': False,
        'default': False
    },
    'negative_prompt': {
        'type': str,
        'required': False,
        'default': ''
    },
    'eta': {
        'type': int,
        'required': False,
        'default': 0
    },
    's_min_uncond': {
        'type': int,
        'required': False,
        'default': 0
    },
    's_churn': {
        'type': int,
        'required': False,
        'default': 0
    },
    's_tmax': {
        'type': int,
        'required': False,
        'default': 0
    },
    's_tmin': {
        'type': int,
        'required': False,
        'default': 0
    },
    's_noise': {
        'type': int,
        'required': False,
        'default': 0
    },
    'override_settings': {
        'type': dict,
        'required': False,
        'default': {}
    },
    'override_settings_restore_afterwards': {
        'type': bool,
        'required': False,
        'default': True
    },
    'script_args': {
        'type': list,
        'required': False,
        'default': []
    },
    'sampler_index': {
        'type': str,
        'required': False,
        'default': 'Euler a',
        'constraints': lambda sampler_name: sampler_name in [
            'Euler a',
            'Euler',
            'LMS',
            'Heun',
            'DPM2',
            'DPM2 a',
            'DPM++ 2S a',
            'DPM++ 2M',
            'DPM++ SDE',
            'DPM++ 2M SDE',
            'DPM fast',
            'DPM adaptive',
            'LMS Karras',
            'DPM2 Karras',
            'DPM2 a Karras',
            'DPM++ 2S a Karras',
            'DPM++ 2M Karras',
            'DPM++ SDE Karras',
            'DPM++ 2M SDE Karras',
            'DDIM',
            'PLMS',
            'UniPC'
        ]
    },
    'script_name': {
        'type': str,
        'required': False,
        'default': ''
    },
    'send_images': {
        'type': bool,
        'required': False,
        'default': True
    },
    'save_images': {
        'type': bool,
        'required': False,
        'default': False
    },
    'alwayson_scripts': {
        'type': dict,
        'required': False,
        'default': {}
    }
}
