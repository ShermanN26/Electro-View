The Core Purpose
This is a high-speed motion detection system designed to turn a standard camera into an automated security guard.
The Three Main Parts
The "Eyes" (120 FPS): It watches the "frontier" at a very high frame rate. This ensures that even fast-moving objects are caught without motion blur.
The "Brain" (Python/OpenCV): It uses math to compare snapshots. If pixels change between frames, the brain realizes something is moving. It’s smart enough to ignore tiny movements (like a fly) and only alert you to big ones (like a person).
The "Alert" (UI): It provides a visual dashboard (HTML/JS) that screams "Intruder Detected!" and draws a red box around the movement so you know exactly where the threat is.
Why It's "Tech Deputy" Grade
Speed: Running at 120 FPS makes it "quick on the draw."
Accuracy: It uses "Noise Filtering" to prevent the alarm from going off for no reason.
Flexibility: It can run in a web browser for easy viewing or as a heavy-duty Python script for professional recording.
