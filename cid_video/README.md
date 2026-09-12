# CID Realistic AI Video Workflow

This folder contains a complete workflow plan for a 60-second CID-style comedy short.

## Video
- Duration: 60 seconds
- Structure: 6 x 10-second clips
- Format: 9:16 vertical
- Style: realistic live-action police procedural comedy
- Story: CID investigates a suspicious chicken murder case
- Final assembly: FFmpeg
- Generation backend: ComfyUI with a compatible text-to-video/image-to-video model (for example Seedance-compatible workflow)

> GitHub stores the workflow and prompts. It does not itself render AI video. Run the generation workflow in a compatible ComfyUI environment with the required model/API access.

## Characters
- ACP Pradyuman: senior Indian police officer, authoritative, serious expression, formal CID-style police uniform.
- Inspector Daya: tall, muscular police inspector, formal CID-style police uniform, alert and energetic.
- Inspector Abhijeet: experienced police inspector, formal CID-style police uniform, observant and calm.
- Dr. Salunkhe: forensic doctor, white lab coat over formal clothes, glasses, analytical and slightly comic.
- Chicken: realistic white/brown hen, identical appearance in every scene.

## Scene files
1. `prompts/scene_01.txt` — crime scene introduction
2. `prompts/scene_02.txt` — egg evidence
3. `prompts/scene_03.txt` — forensic examination
4. `prompts/scene_04.txt` — suspicious stare
5. `prompts/scene_05.txt` — chicken interrogation
6. `prompts/scene_06.txt` — comic ending

## Generation workflow
1. Load the JSON workflow specification in `workflows/CID_6x10s_Realistic.json` and adapt node/model names to the installed ComfyUI backend.
2. Generate each scene as a separate 10-second 9:16 clip.
3. Keep the character/environment lock from `prompts/character_lock.txt` at the start of every generation prompt.
4. Use the same seed/reference images where the chosen model supports them.
5. Save clips as `scene_01.mp4` through `scene_06.mp4`.
6. Put the six clips into `output/clips/`.
7. Run `scripts/assemble_video.py` to create `output/CID_Murghi_Murder_60s.mp4`.

## Audio
The scene prompts contain dialogue for lip-sync. If the selected video model does not generate reliable speech, generate video first and add Urdu/Hindi voiceover in a separate audio pass.

## Content note
This is fan-style CID comedy content and is not presented as an official CID production.
