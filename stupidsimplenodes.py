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

NODE_CLASS_MAPPINGS = {
    "Stupid Simple Seed (INT)": SSN_Seed_INT,
}    