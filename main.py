#!/usr/bin/env python3.7

"""Start IMA-Monitoring Plataform"""
from core import controllerAPI

api = controllerAPI.ControllerRestfulAPI()
api.run()
