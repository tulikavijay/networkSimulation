## Network Simulation

### Usage

Fork the repoistory :
```
git clone git@github.com:tulikavijay
```

#### Docker

The web application can be run within docker using [docker-compose](https://docs.docker.com/install/overview/).

To build and run the application:

```
docker-compose up -- build
```


### Details

A connection in a network can have many devices. In this network we have computers and repeaters
Connections (wired/wireless) between devices can transfer information both ways.
When information must be transferred between two devices and if there is no direct connection between two devices, it must be transferred from device to device until it reaches the destination.

1. The message sent by a device has a ‘strength’, limiting it to travel only a specific distance.
1. The strength of a message will reduce by 1 unit after every device it reaches from the source computer.
1. If the message being sent encounters a repeater, it’s strength will be amplified by double its current strength.

Commands:
1. Add a device to a network.
1. Add connections between two devices.
1. List all the devices
1. To fetch the route that must be taken if the information is to be passed between two devices.
1. To set device strength

#### ADD DEVICE
CREATE /devices
content-type : application/json
{"type" : "COMPUTER", "name" : "A1"}

Every device must have a unique name (at least one character).
The device type must be an enumeration of either ‘COMPUTER’ or ‘REPEATER’.


#### CONNECT DEVICES
CREATE /connections
content-type : application/json
{"source" : "A1", "targets" : ["A2"]}'

1. A device cannot be connected to itself.
1. A device can be connected to any number of devices.
1. A device does not necessarily need to be connected to other devices

#### LIST DEVICES
FETCH /devices

List all devices in the network

#### ROUTE INFO
FETCH /info-routes?from=A1&to=A2

If no route is found between two devices, then an error message must be displayed.
The route for a device to itself should only have a source and destination which are both itself.
The source or the destination device cannot be a repeater.

#### CHANGE DEVICE STRENGTH
MODIFY /devices/A1/strength
content-type : application/json
{"value": 2}

The strength defined for a device must be a number and it cannot be negative.
