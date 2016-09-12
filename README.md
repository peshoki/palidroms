# palidroms

How to use:

0. Clone this repo.
 
  ```
  git clone https://github.com/peshoki/palidroms.git
  ```
0. Build docker image.
  
  ```
  cd palidroms/
  sudo docker build --no-cache -t palidroms .
  ```
0. Run tests.
  
  ```
  sudo docker run -it --rm palidroms python setup.py test
  ```
0. Run chalange.
  ```
  sudo docker run -it --rm palidroms palidroms
  ```
0. Enjoy
