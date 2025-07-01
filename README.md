# ha-echo-command-center
Alexa Skill includes LAMBDA script, python_script, home assistant scripts and automation for last_called device to work with purposed intents

# Helpers
Create 2 helpers. The first is a simple input_text helper called "input_text.alexa_last_device". The second is a template sensor. I created mine in yaml. It looks like this - 

  - sensor:
      - name: "Resolved Echo Target"
        unique_id: echo_target
        state: "{{ states('sensor.echo_target') }}"
        attributes:
          friendly_name: "Resolved Echo Target"
