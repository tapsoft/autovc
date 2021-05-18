Wave file structure example:

```
/wavs/p1 (for person 1)
+-- p1-001.wav
+-- p1-002.wav
+-- p1-003.wav
+-- p1-004.wav
+-- p1-005.wav
+-- p1-006.wav
+-- p1-007.wav
+-- p1-008.wav
+-- p1-009.wav
+-- p1-010.wav
/wavs/p2 (for person 2)
+-- p2-001.wav
+-- p2-002.wav
+-- p2-003.wav
+-- p2-004.wav
+-- p2-005.wav
+-- p2-006.wav
+-- p2-007.wav
+-- p2-008.wav
+-- p2-009.wav
+-- p2-010.wav
/wavs/p3 (for person 3)
...
```

Number of .wav files in each person's folder must be same as `num_uttrs` variable in `make_metadata.py`.
