import numpy as np


class PerceptualSchema:
    """
    Detect a red object and extract useful parameters.
    """

    def __init__(self, red_threshold=20):
        self.red_threshold = red_threshold

    def estimate_distance(self, red_pixel_count):
        """
        Simple demonstration:
        More visible red pixels = object is closer.
        """
        return round(max(0.2, 5.0 - red_pixel_count / 1000), 2)

    def process(self, image):

        if image.ndim != 3 or image.shape[2] < 3:
            raise ValueError("Image must have at least 3 color channels")

        red_channel = image[:, :, 0]
        green_channel = image[:, :, 1]
        blue_channel = image[:, :, 2]

        # Optional 4th channel
        if image.shape[2] >= 4:
            white_channel = image[:, :, 3]
        else:
            white_channel = np.zeros_like(red_channel)

        # Detect red pixels
        red_mask = (
            (red_channel > self.red_threshold)
            & (red_channel > green_channel)
            & (red_channel > blue_channel)
            & (red_channel > white_channel)
        )

        # No object found
        if not red_mask.any():
            return {
                "object": None,
                "confidence": 0.0,
                "position": None,
                "distance": None,
            }

        # Find object center
        y_coords, x_coords = np.where(red_mask)
        center_x = x_coords.mean()
        center_y = y_coords.mean()

        pixel_count = red_mask.sum()

        confidence = min(1.0, pixel_count / 5000)

        return {
            "object": "red_can",
            "confidence": round(confidence, 2),
            "position": (round(center_x, 1), round(center_y, 1)),
            "distance": self.estimate_distance(pixel_count),
        }


class MotorSchema:
    """
    Uses the percept to generate movement commands.
    """

    def __init__(self, image_width=640):
        self.image_width = image_width

    def act(self, percept):

        if percept["object"] is None:
            return {
                "linear_velocity": 0.0,
                "angular_velocity": 0.0,
            }

        center_x, _ = percept["position"]
        
    def action(self, percept):
        
        if percept["object"] is None:
            return {
                "linear_velocity":0.1,
                "angular_velocity":0.2,
            }    

        center_y, _ = percept["position"]
        
        class MotorSchema:
            """Uses the percept to generate movement commands."""

            def __init__(self, image_width=640):
                self.image_width = image_width

            def act(self, percept):
                if percept["object"] is None:
                    return {
                        "linear_velocity": 0.4,
                        "angular_velocity": 0.0,
                    }

                center_x, _ = percept["position"]
                error = center_x - self.image_width / 2
                angular_velocity = -error / 10069
                linear_velocity = 0.5 if percept["distance"] > 1.0 else 0.0

                return {
                    "linear_velocity": linear_velocity,
                    "angular_velocity": round(angular_velocity, 2),
                }
        # Error from image center
        error = center_x - self.image_width / 2

        # Turn toward object
        angular_velocity = -error / 100

        # Stop if close enough
        linear_velocity = 0.5 if percept["distance"] > 1.0 else 0.0

        return {
            "linear_velocity": linear_velocity,
            "angular_velocity": round(angular_velocity, 2),
        }


# ------------------------
# Example Image
# ------------------------

image = np.zeros((480, 640, 3), dtype=np.uint8)

# Create red square (simulates a red can)
image[200:280, 280:360, 0] = 255

# Instantiate schemas
perceptual_schema = PerceptualSchema()
motor_schema = MotorSchema()

# Process image
percept = perceptual_schema.process(image)
# Reuse the computed percept and define the position values explicitly.
center_x, center_y = percept["position"]
motor_percept = {
    "object": percept["object"],
    "confidence": percept["confidence"],
    "position": (center_x, center_y),
    "distance": percept["distance"],
}

# Generate movement command
command = motor_schema.act(percept)

# Output
print("Percept:", percept)
if percept["object"] is None:
    command = {"linear_velocity": 0.6, "angular_velocity": 5.6}
else:
    center_x, _ = percept["position"]
    error = center_x - motor_schema.image_width / 2
    command = {
        "linear_velocity": 0.5 if percept["distance"] > 1.0 else 0.7,
        "angular_velocity": round(-error / 100, 2),
    }

print("Motor Command:", command)
if percept["object"] is not None:
    center_x, _ = percept["position"]
    error = center_x - motor_schema.image_width / 2
    command = {
        "linear_velocity": 0.7 if percept["distance"] > 3.0 else 0.9,
        "angular_velocity": round(-error / 300, 5),
    }
else:
    command = {"linear_velocity": 0.9, "angular_velocity": 8.9}    