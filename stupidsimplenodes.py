import comfy.samplers


class SSN_Seed_INT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
                    }
                }

    RETURN_TYPES = ("INT",)
    FUNCTION = "seed"

    CATEGORY = "StupidSimpleNodes"

    def seed(self, seed):
        return (int(seed), )


class SSN_INT_INT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "integer": ("INT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff})
                    }
                }

    RETURN_TYPES = ("INT",)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, integer):
        return (int(integer), )


class SSN_FLOAT_FLOAT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "floatnum": ("FLOAT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff})
                    }
                }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, floatnum):
        return (float(floatnum), )


class SSN_Math_Add_INT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "var1": ("INT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff}),
                        "var2": ("INT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff})
                    }
                }

    RETURN_TYPES = ("INT",)
    FUNCTION = "add"

    CATEGORY = "StupidSimpleNodes"

    def add(self, var1, var2):
        return (int(var1)+int(var2), )


class SSN_Math_Add_FLOAT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "var1": ("FLOAT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff}),
                        "var2": ("FLOAT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff})
                    }
                }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "add"

    CATEGORY = "StupidSimpleNodes"

    def add(self, var1, var2):
        return (float(var1)+float(var2), )


class SSN_Math_Mul_INT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "var1": ("INT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff}),
                        "var2": ("INT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff})
                    }
                }

    RETURN_TYPES = ("INT",)
    FUNCTION = "add"

    CATEGORY = "StupidSimpleNodes"

    def add(self, var1, var2):
        return (int(var1)*int(var2), )


class SSN_Math_Mul_FLOAT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "var1": ("FLOAT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff}),
                        "var2": ("FLOAT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff})
                    }
                }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "add"

    CATEGORY = "StupidSimpleNodes"

    def add(self, var1, var2):
        return (float(var1)*float(var2), )


class SSN_SAMPLER:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "sampler": (comfy.samplers.KSampler.SAMPLERS,),
                    }
                }

    RETURN_TYPES = (comfy.samplers.KSampler.SAMPLERS,)
    RETURN_NAMES = ("COMBO_SAMPLERS",)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, sampler):
        return (sampler, )

class SSN_SCHEDULER:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "scheduler": (comfy.samplers.KSampler.SCHEDULERS,),
                    }
                }

    RETURN_TYPES = (comfy.samplers.KSampler.SCHEDULERS,)
    RETURN_NAMES = ("COMBO_SCHEDULERS",)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, scheduler):
        return (scheduler, )


class SSN_STRING:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "string": ("STRING", {"multiline": False}),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, string):
        return (string, )


class SSN_TEXT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "text": ("STRING", {"multiline": True}),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, text):
        return (text, )


class SSN_REROUTE_MODEL:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "model": ("MODEL",),
                    }
                }

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, model):
        return (model, )


class SSN_REROUTE_CLIP:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "clip": ("CLIP",),
                    }
                }

    RETURN_TYPES = ("CLIP",)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, clip):
        return (clip, )


class SSN_REROUTE_VAE:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "vae": ("VAE",),
                    }
                }

    RETURN_TYPES = ("VAE",)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, vae):
        return (vae, )


class SSN_REROUTE_LATENT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "latent": ("LATENT",),
                    }
                }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, latent):
        return (latent, )


NODE_CLASS_MAPPINGS = {
    "Stupid Simple Seed (INT)": SSN_Seed_INT,
    "Stupid Simple Addition (INT)": SSN_Math_Add_INT,
    "Stupid Simple Addition (FLOAT)": SSN_Math_Add_FLOAT,
    "Stupid Simple Multiplier (INT)": SSN_Math_Mul_INT,
    "Stupid Simple Multiplier (FLOAT)": SSN_Math_Mul_FLOAT,
    "Stupid Simple Number (INT)": SSN_INT_INT,
    "Stupid Simple Number (FLOAT)": SSN_FLOAT_FLOAT,
    "Stupid Simple String": SSN_STRING,
    "Stupid Simple Text": SSN_TEXT,
    "Stupid Simple Sampler": SSN_SAMPLER,
    "Stupid Simple Rerouter (MODEL)": SSN_REROUTE_MODEL,
    "Stupid Simple Rerouter (CLIP)": SSN_REROUTE_CLIP,
    "Stupid Simple Rerouter (VAE)": SSN_REROUTE_VAE,
    "Stupid Simple Rerouter (LATENT)": SSN_REROUTE_LATENT
}
