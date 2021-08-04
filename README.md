# introduction:

    Application Server that creates a buffer for orders and sends them to a mocked execution server

#### - Endpoints: 
    /v1/server/order/create

#### - input:
    the following json:


    {   
        "amount": 100,
        "commandType": "BUY",
        "dst": "b",
        "src": "a"
    }

#### - how to run
    docker build -t edgify .
    docker run -it --rm -p 6666:6666 -e PORT='6666' edgify

    * send a postman request to : 127.0.0.1:6666/v1/server/order/create 
    with the desired input