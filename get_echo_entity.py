device_map = {
    "amzn1.ask.device.device_id_1": "media_player.kitchen_echo_show",
    "amzn1.ask.device.device_id_2": "media_player.basement_echo_dot_1",
    "amzn1.ask.device.device_id_3": "media_player.family_room_fire_stick",
    "amzn1.ask.device.device_id_4": "media_player.main_bathroom_echo_flex",
    "amzn1.ask.device.device_id_5": "media_player.garage_echo_dot",
    "amzn1.ask.device.device_id_6": "media_player.mere_s_echo_dot",
    "amzn1.ask.device.device_id_7": "media_player.basement_echo_dot_2",
    "amzn1.ask.device.device_id_8": "media_player.master_bedroom_echo_show",
    "amzn1.ask.device.device_id_9": "media_player.sunroom_echo_dot",
    "amzn1.ask.device.device_id_10": "media_player.emma_s_echo_dot",
    "amzn1.ask.device.device_id_11": "media_player.family_room_echo_dot",
    "amzn1.ask.device.device_id_12": "media_player.my_fire_stick",
    "amzn1.ask.device.device_id_13": "media_player.living_room_fire_tv_cube"
}

device_id = data.get("device_id", "")
entity_id = device_map.get(device_id, "media_player.kitchen_echo_show")

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
