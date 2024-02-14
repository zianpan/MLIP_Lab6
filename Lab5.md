# Lab 5 - Continuous Integration with Jenkins

In this lab, you will explore how to perform Continuous Integration(CI) using Jenkins.
Jenkins has a wide range of functionalities that facilitate the software development process. In this lab, we will focus on the Continuous Integration aspect, which means updates to the code base are continuously tested to ensure the program's quality.
To receive credit for this lab, show your work to the TA during recitation.

## Deliverables
- [ ] Demonstrate the successful installation of Java and Jenkins on the team virtual machine (recommended) or your location machine.
- [ ] Adding the "avg length ratio" Zeno metric to your project
- [ ] Create 2/3 slices and derive meaningful insights and showcase them to the TA 

## Java Installation
- Go to [Jenkins Installation Page](https://www.jenkins.io/doc/book/installing/), select the Operating System you currently use. For your team server, please select [linux](https://www.jenkins.io/doc/book/installing/linux/).
- Under section [Installation of Java](https://www.jenkins.io/doc/book/installing/linux/#installation-of-java), install java using command: `sudo apt install fontconfig openjdk-17-jre`.
- Show the success of installation by running `java --version`

## Jenkins Installation
- In the same page we use in **Java Installation**, locate the installation command for Jenkins. For linux ubuntu system, it's:
  ```sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
    https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
  echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null
  sudo apt-get update
  sudo apt-get install jenkins
  ```
- Use command `sudo systemctl start jenkins` to start Jenkins server.
- Show the success of Jenkins installation by running `sudo systemctl status jenkins`

## Installation instructions
- python 3.10 version is needed for the zeno packages to run correctly
- pip install packaging ~ version 23.2

## Code related details
- Replace the API key in the started code
- Create the project and verify if you can access your project on the hub
- Finish all 6 steps mentioned in the python notebook 
- Verify if the data has been uploaded on the zeno hub project you created
- Go back to Step 2 - Uncomment this line -> ZenoMetric(name="avg length ratio", type="mean", columns=["avg_length_ratio"])
- Go back to Step 3 - Uncomment the last line -> Complete the function to calculate the avg length ratio
- Upload the system outputs again and verify if the newly added metric has been reflected

## Additional resources
- [Zeno Getting Started](https://zenoml.com/docs/intro)
- [Exploring Zeno Projects] (https://hub.zenoml.com/home)
