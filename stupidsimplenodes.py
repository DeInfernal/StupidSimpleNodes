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
                        "INTEGER": ("INT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff})
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
                        "FLOATNUM": ("FLOAT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff})
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

class SSN_SAMPLER:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "sampler": (comfy.samplers.KSampler.SAMPLERS, ),
                    }
                }

    RETURN_TYPES = (comfy.samplers.KSampler.SAMPLERS,)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, sampler):
        return (sampler, )

class SSN_SCHEDULER:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                    }
                }

    RETURN_TYPES = (comfy.samplers.KSampler.SCHEDULERS,)
    FUNCTION = "func"

    CATEGORY = "StupidSimpleNodes"

    def func(self, scheduler):
        return (scheduler, )

NODE_CLASS_MAPPINGS = {
    "Stupid Simple Seed (INT)": SSN_Seed_INT,
    "Stupid Simple Addition (INT)": SSN_Math_Add_INT,
    "Stupid Simple Number (INT)": SSN_INT_INT,
    "Stupid Simple Number (FLOAT)": SSN_FLOAT_FLOAT,
    "Stupid Simple Sampler": SSN_SAMPLER,
    "Stupid Simple Scheduler": SSN_SCHEDULER
}    