#include <iostream>
#include "tools.h"

using Eigen::VectorXd;
using Eigen::MatrixXd;
using std::vector;

Tools::Tools() {}

Tools::~Tools() {}

VectorXd Tools::CalculateRMSE(const vector<VectorXd> &estimations,
                              const vector<VectorXd> &ground_truth) {
    VectorXd rmse(4);
    rmse << 0,0,0,0;

    if(!estimations.size() || estimations.size() != ground_truth.size()){
        cout << "Error on vectors sizes" << endl;
        exit(-1);
    }

    for(unsigned int i=0; i < estimations.size(); ++i){
        VectorXd ac = (estimations[i]-ground_truth[i]);
        ac = ac.array() * ac.array();
        rmse += ac;
    }

    //calculate the mean
    rmse /= estimations.size();

    //calculate the squared root
    rmse = rmse.array().sqrt();

    //return the result
    return rmse;
}
