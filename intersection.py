import cv2

Rect A(20,20,80,80); // blue
Rect B(60,60,60,60); // blue

Rect C = A & B;   // red
Rect D = A | B;   // green

cerr << "A" << A << endl;
cerr << "B" << B << endl;
cerr << "C" << C << endl;
cerr << "D" << D << endl;

Mat draw(200,200,CV_8UC3,Scalar::all(0));
rectangle(draw,A,Scalar(200,0,0),2);
rectangle(draw,B,Scalar(200,0,0),2);
rectangle(draw,C,Scalar(0,0,200),1);
rectangle(draw,D,Scalar(0,200,0),1);