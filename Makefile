# Copyright 2013 Prometheus Team
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

KEY_ID ?= _DEFINE_ME_

JARNAME := model-0.0.4-SNAPSHOT.jar
PROTOS  := metrics.proto prometheus.proto

all: cpp go java python

SUFFIXES:

cpp: cpp/prometheus.pb.cc cpp/prometheus.pb.h

cpp/prometheus.pb.cc: $(PROTOS)
	protoc $^ --cpp_out=cpp/

cpp/prometheus.pb.h: $(PROTOS)
	protoc $^ --cpp_out=cpp/

go: go/prometheus.pb.go

go/prometheus.pb.go: $(PROTOS)
	protoc $^ --go_out=go/

java: target/$(JARNAME)

target/$(JARNAME): src/main/java/io/prometheus/client/Prometheus.java pom.xml
	mvn clean compile package

src/main/java/io/prometheus/client/Prometheus.java: $(PROTOS)
	protoc $^ --java_out=src/main/java

python: python/prometheus/client/model/prometheus_pb2.py

python/prometheus/client/model/prometheus_pb2.py: $(PROTOS)
	-mkdir -p $(@D)
	protoc $^ --python_out=$(@D)

clean:
	-rm -rf cpp/*.pb.{cc,h}
	-rm -rf go/*.pb.go
	-rm -rf src/main/java/*
	- find python/ -name "*_pb2.py" -delete
	-mvn clean

maven-deploy-snapshot: java
	mvn clean deploy -Dgpg.keyname=$(KEY_ID) -DperformRelease=true

maven-deploy-release: java
	mvn clean release:clean release:prepare release:perform -Dgpg.keyname=$(KEY_ID) -DperformRelease=true

.PHONY: all clean cpp go java maven-deploy-snapshot maven-deploy-release python
