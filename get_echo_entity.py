device_map = {
    "amzn1.ask.device.device_id_1": "notify.kitchen_echo_show_speak",
    "amzn1.ask.device.device_id_2": "notify.basement_echo_dot_1_speak",
    "amzn1.ask.device.device_id_3": "notify.family_room_fire_stick_speak",
    "amzn1.ask.device.device_id_4": "notify.main_bathroom_echo_flex_speak",
    "amzn1.ask.device.device_id_5": "notify.garage_echo_dot_speak",
    "amzn1.ask.device.device_id_6": "notify.bedroom_1_echo_dot_speak",
    "amzn1.ask.device.device_id_7": "notify.basement_echo_dot_2_speak",
    "amzn1.ask.device.device_id_8": "notify.master_bedroom_echo_show_speak",
    "amzn1.ask.device.device_id_9": "notify.sunroom_echo_dot_speak",
    "amzn1.ask.device.device_id_10": "notify.bedroom_2_echo_dot_speak",
    "amzn1.ask.device.device_id_11": "notify.family_room_echo_dot_speak",
    "amzn1.ask.device.device_id_12": "notify.my_fire_stick_speak",
    "amzn1.ask.device.device_id_13": "notify.living_room_fire_tv_cube_speak"
}

device_id = data.get("device_id", "")
entity_id = device_map.get(device_id, "notify.kitchen_echo_show_speak")

# Only update if needed
current_value = hass.states.get("input_text.alexa_last_device")
current_value = current_value.state if current_value else ""

if current_value != entity_id:
    try:
        hass.services.call("input_text", "set_value", {
            "entity_id": "input_text.alexa_last_device",
            "value": entity_id
        }, blocking=False)  # set blocking=False to avoid lock on waits
    except Exception as e:
        logger.warning(f"Failed to set input_text.alexa_last_device due to: {e}")

# Always update the sensor so automations can react
hass.states.set("sensor.echo_target", entity_id, {
    "source": device_id
})
