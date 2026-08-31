#part 1:Ask the agent for their details
name= input("Enter your real name, Agent: ")
gadget= input("Enter your favourite gadget: ")


agent_number=7
speed_rating=9.5
mission_count=12
height_m=1.65
is_active=True


print("Name:", name, "-> type:", type(name))
print("Gadget:", gadget, "-> type:", type(gadget))
print("Agent Number:", agent_number, "-> type:", type(agent_number))
print("Speed Rating:", speed_rating, "-> type:", type(speed_rating))
print("mission:", mission_count, "-> type:", type(mission_count))
print("height_m:", name, "-> height_m:", type(height_m))
print("is_active:", is_active, "-> type:", type(is_active))

agent_number_text= str(agent_number)
mission_count_text= str(mission_count)
speed_rating_text= str(speed_rating)
status_text=str(is_active)

print("Agent Number as text:", agent_number_text, "->  type:",
     type(agent_number_text))
print("Mission Count as text:", mission_count_text, "->  type:",
     type(mission_count_text))
print("Speed Rating as text:", speed_rating_text, "->  type:",
     type(speed_rating_text))

first_three=name[0:3]
last_letter=name[-1:]
code_name=first_three + last_letter
print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Secret Code name:", code_name)

reserved_gadget= gadget[::-1]
print("Reserved Gadget Name:", reserved_gadget)

badge_line_1="AGENT" + code_name.upper()
badge_line_2="SECRET GADGET CODE" + reserved_gadget.upper()