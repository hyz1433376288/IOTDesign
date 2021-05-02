import include.Decode
import include.Encode
import json
def listen_web():
    return False
def code_to_json(code_obj):
    data = {
        'src_addr': code_obj.src_addr,
        'des_addr': code_obj.des_addr,
        'temperature_cnt': code_obj.temperature_cnt,
        'temperature': code_obj.temperature,
        'humidity_cnt': code_obj.humidity_cnt,
        'humidity.txt': code_obj.humidity,
        'airconditioner_cnt': code_obj.airconditioner_cnt,
        'airconditioner': code_obj.airconditioner,
        'light_turn_cnt': code_obj.light_turn_cnt,
        'light_turn': code_obj.light_turn,
        'light_adjust_cnt': code_obj.light_adjust_cnt,
        'light_adjust': code_obj.light_adjust,
        'window_cnt': code_obj.window_cnt,
        'window': code_obj.window
    }
    return json