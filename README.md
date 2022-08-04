# AI-Chess-Position
AI Chess Position Kaggle Competition :chess:

## **AI Chess Master - Computer Vision Final**
**Author:** Ibrahim Sobh

**Instructions:**

This **notebook** includes:
* Data Exploration ✅
* Models Training ✅
* Performance Evaluation ✅
* Saving Model for Production ✅

**Dataset** https://www.kaggle.com/datasets/koryakinp/chess-positions?datasetId=115231/br>
**My Kaggle Published Notebook** https://www.kaggle.com/code/ibrahimsoboh/chess-positions-fen-prediction-eda-cnn-model </br>



## Introduction:
This project tackles the problem of detecting chessboards positions captured in 2D Chess Boards images. A chessboard board consists of 64 squares (eight rows and eight columns) and the chess pieces that are placed on a board.
The problem of recognizing a chessboard from an image can be difficult, with a major issue mostly being the quality of images (lighting issues and low resolutions images).
For this reason, most current methods for chessboard recognition typically perform certain simplifications. This includes utilizing only a single chessboard style during experiments, capturing images with adirect overhead view of the chessboard (in Case of 2D Chess Board Recognition ) or at a convenient angle specified in advanced ( in Case of 3D Chess Board Recognition).
The state of the art to solve this problem is using a CNN’s that feeds on the chess Board blocks (for each image we chop it into 64 blocks representing 64 position/ possible piece). Afterwards we encode the labels into classes (multiclass classification) to get the result and then we decode the results to reproduce the images of predicted FEN’s.
Chessboards Forsyth–Edwards Notation (FEN for short) is a standard notation for describing a particular board position of a chess game. The purpose of FEN is to provide all the necessary information to restart a game from a particular position, FEN is used to define initial positions oth. Usually (Capital Letters for White) (small Letters for Black)



![output-onlinepngtools](https://user-images.githubusercontent.com/49615833/182905540-68cc56a2-d651-4439-89a7-be09a07be866.png)


Example in the picture above: 7B-8-1RK2B2-5NR1-4q2p-1P6-2k2P2-2B2N27

7B     -> means & empty spaces then Bishop (White)    
8      -> means empty row 
1RK2B2 -> means one empty spaces , a Rook(White), a King White),2 spaces … etc.
Methodology:
The dataset I used in this project is tske
dataset description, tested models explanation (1 page max). 
Results: describe your performances and the evaluation metrics you selected (2 pages max). 
○ Conclusion and perspectives (1 page max). 


## Results

![Screenshot 2022-08-04 at 10 12 54 PM](https://user-images.githubusercontent.com/49615833/182951915-66c95aae-7b6f-4cda-ba5d-a39f40196f52.png)![Screenshot 2022-08-04 at 10 19 05 PM](https://user-images.githubusercontent.com/49615833/182951928-6668c7f5-911b-414a-99a1-beaf83b64482.png)


