# ECG-Denoise
The ecg signal tainted with random noise, baseline wander noise, powerline interference was de-noised using a combination of synchronized averaging and FIR filters using various windowingtechniques, to detect R peak of the QRS complex.

# Input
The noisy signal tainted with baseline wander noise, powerline interference after the random noise removal.<br/>
![Alt text](noisy_signal.PNG?raw=true "Title")

# Filtering
Hamming window based FIR filtering is depicted. <br/>
![Alt text](hamming_filter_reconstruction.PNG?raw=true "Title")


# Output
Generated beat rate after R peak detection. <br/>
![Alt text](beatRate.PNG?raw=true "Title")
