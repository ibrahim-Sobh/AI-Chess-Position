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

**Dataset** https://www.kaggle.com/code/jayshworkhadka/chess-fen-prediction </br>
**My Kaggle Published Notebook** https://www.kaggle.com/code/ibrahimsoboh/chess-positions-fen-prediction-eda-cnn-model </br>



1. Introduction:
This project tackles the problem of detecting chessboards positions captured in 2D Chess Boards images. A chessboard board consists of 64 squares (eight rows and eight columns) and the chess pieces that are placed on a board.
The problem of recognizing a chessboard from an image can be difficult, with a major issue mostly being the quality of images (lighting issues and low resolutions images).
For this reason, most current methods for chessboard recognition typically perform certain simplifications. This includes utilizing only a single chessboard style during experiments, capturing images with adirect overhead view of the chessboard (in Case of 2D Chess Board Recognition ) or at a convenient angle specified in advanced ( in Case of 3D Chess Board Recognition).
The state of the art to solve this problem is using a CNN’s that feeds on the chess Board blocks (for each image we chop it into 64 blocks representing 64 position/ possible piece). Afterwards we encode the labels into classes (multiclass classification) to get the result and then we decode the results to reproduce the images of predicted FEN’s.
Chessboards Forsyth–Edwards Notation (FEN for short) is a standard notation for describing a particular board position of a chess game. The purpose of FEN is to provide all the necessary information to restart a game from a particular position, FEN is used to define initial positions oth. Usually (Capital Letters for White) (small Letters for Black)

Example in the picture above: 7B-8-1RK2B2-5NR1-4q2p-1P6-2k2P2-2B2N27
[output.svg.pdf](https://github.com/ibrahim-Sobh/AI-Chess-Position/files/9261619/output.svg.pdf)


7B     -> means & empty spaces then Bishop (White)    
8      -> means empty row 
1RK2B2 -> means one empty spaces , a Rook(White), a King White),2 spaces … etc.
Methodology:
The dataset I used in this project is tske
dataset description, tested models explanation (1 page max). 
Results: describe your performances and the evaluation metrics you selected (2 pages max). 
○ Conclusion and perspectives (1 page max). 
 

