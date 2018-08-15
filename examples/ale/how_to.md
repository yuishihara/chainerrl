- To evaluate and save frames
python train_dqn_ale.py --gpu=0 --env=FreewayNoFrameskip-v4 --replay-memory-size=500000 --monitor --render --demo --load=results/20180809T215030.017465/18400135 --eval-epsilon=0.3 --eval-n-runs=100

