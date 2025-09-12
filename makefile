docker:
	docker build -t test_lambda .
	docker tag test_lambda:latest 196980042128.dkr.ecr.ap-south-1.amazonaws.com/test_lambda:latest
	docker push 196980042128.dkr.ecr.ap-south-1.amazonaws.com/test_lambda:latest
