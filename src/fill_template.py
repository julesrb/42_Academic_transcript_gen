import json
from jinja2 import Template
from datetime import datetime


def fill_template():

	# Load JSON data
	with open("./data/user.json") as f:
		data = json.load(f)

	with open("./projects/projects_dict.json") as f:
		pj_dic = json.load(f)

	def parse_projects(data, pj_dic):
		parsed = {}
		for entry in data["projects_users"]:
			project = entry.get("project", {})
			project_name = project.get("name")
			if project_name:
				# Parse the marked_at date once
				marked_at_str = entry.get("marked_at")
				marked_at = None
				if marked_at_str:
					try:
						marked_at = datetime.fromisoformat(marked_at_str.replace("Z", "+00:00"))
					except ValueError:
						marked_at = None  # or log/raise depending on how strict you want to be
				project_id = str(project.get("id"))
				project_data = pj_dic.get(project_id, {})
				parsed[project_name] = {
					"id": project_id,
					"name": project_data.get("name"),
					"validated": entry.get("validated?"),
					"marked_at": marked_at,
					"description": project_data.get("description"),
					"grade": entry.get("final_mark"),
					"hours": project_data.get("hours")
				}
		return parsed
	
	parsed = parse_projects(data, pj_dic)

	with open("./data/user_prj.json", "w", encoding="utf-8") as f:
		json.dump(parsed, f, ensure_ascii=False, indent=4, default=str)

	school_address = """42 Berlin
					Harzer Straße 39
					12059 Berlin
					GERMANY"""
	
	first_name = data["first_name"]
	last_name = data["last_name"]
	date_of_birth = "-coming soon-"
	date_issued = datetime.today().strftime("%B %d, %Y")

	passed_selection = data["pool_month"].capitalize() + " " + data["pool_year"]
	core_started = "November 28, 2022"

	tran = parsed.get("ft_transcendence")
	exam = parsed.get("Exam Rank 06")

	if all([tran, exam, tran.get("validated"), exam.get("validated")]):
		dt = max(tran["marked_at"], exam["marked_at"])
		core_completed = dt.strftime("%B %-d, %Y")  # Use "%B %d, %Y" on Windows
	else:
		core_completed = "in progress"

	# TODO add logic to get the date here
	advanced_completed = "in progress" 

	# Rank 0
	rank0 = []
	if parsed.get("Libft", {}).get("validated"):
		rank0.append(parsed["Libft"])

	# Rank 1
	rank1 = []
	if parsed.get("ft_printf", {}).get("validated"):
		rank1.append(parsed["ft_printf"])
	if parsed.get("Born2beroot", {}).get("validated"):
		rank1.append(parsed["Born2beroot"])
	if parsed.get("get_next_line", {}).get("validated"):
		rank1.append(parsed["get_next_line"])

	# Rank 2
	rank2 = []
	if parsed.get("FdF", {}).get("validated"):
		rank2.append(parsed["FdF"])
	if parsed.get("so_long", {}).get("validated"):
		rank2.append(parsed["so_long"])
	if parsed.get("fract-ol", {}).get("validated"):
		rank2.append(parsed["fract-ol"])
	if parsed.get("push_swap", {}).get("validated"):
		rank2.append(parsed["push_swap"])
	if parsed.get("minitalk", {}).get("validated"):
		rank2.append(parsed["minitalk"])
	if parsed.get("pipex", {}).get("validated"):
		rank2.append(parsed["pipex"])

	# Rank 3
	rank3 = []
	if parsed.get("minishell", {}).get("validated"):
		rank3.append(parsed["minishell"])
	if parsed.get("Philosophers", {}).get("validated"):
		rank3.append(parsed["Philosophers"])

	# Rank 4
	rank4 = []
	if parsed.get("cub3d", {}).get("validated"):
		rank4.append(parsed["cub3d"])
	if parsed.get("miniRT", {}).get("validated"):
		rank4.append(parsed["miniRT"])
	if parsed.get("NetPractice", {}).get("validated"):
		rank4.append(parsed["NetPractice"])
	if parsed.get("CPP Module 00", {}).get("validated"):
		rank4.append(parsed["CPP Module 00"])
	if parsed.get("CPP Module 01", {}).get("validated"):
		rank4.append(parsed["CPP Module 01"])
	if parsed.get("CPP Module 02", {}).get("validated"):
		rank4.append(parsed["CPP Module 02"])
	if parsed.get("CPP Module 03", {}).get("validated"):
		rank4.append(parsed["CPP Module 03"])
	if parsed.get("CPP Module 04", {}).get("validated"):
		rank4.append(parsed["CPP Module 04"])

	# Rank 5
	rank5 = []
	if parsed.get("CPP Module 05", {}).get("validated"):
		rank5.append(parsed["CPP Module 05"])
	if parsed.get("CPP Module 06", {}).get("validated"):
		rank5.append(parsed["CPP Module 06"])
	if parsed.get("CPP Module 07", {}).get("validated"):
		rank5.append(parsed["CPP Module 07"])
	if parsed.get("CPP Module 08", {}).get("validated"):
		rank5.append(parsed["CPP Module 08"])
	if parsed.get("CPP Module 09", {}).get("validated"):
		rank5.append(parsed["CPP Module 09"])
	if parsed.get("ft_irc", {}).get("validated"):
		rank5.append(parsed["ft_irc"])
	if parsed.get("webserv", {}).get("validated"):
		rank5.append(parsed["webserv"])
	if parsed.get("Inception", {}).get("validated"):
		rank5.append(parsed["Inception"])


	# Rank 6
	rank6 = []
	if parsed.get("ft_transcendence", {}).get("validated"):
		rank6.append(parsed["ft_transcendence"])

	#AI and Algo
	ai= []
	if parsed.get("gomoku", {}):
		ai.append(parsed["gomoku"])
	if parsed.get("expert-system", {}):
		ai.append(parsed["expert-system"])
	if parsed.get("n-puzzle", {}):
		ai.append(parsed["n-puzzle"])
	if parsed.get("ft_linear_regression", {}):
		ai.append(parsed["ft_linear_regression"])
	if parsed.get("krpsim", {}):
		ai.append(parsed["krpsim"])
	if parsed.get("rubik", {}):
		ai.append(parsed["rubik"])
	if parsed.get("dslr", {}):
		ai.append(parsed["dslr"])
	if parsed.get("multilayer-perceptron", {}):
		ai.append(parsed["multilayer-perceptron"])
	if parsed.get("total-perspective-vortex", {}):
		ai.append(parsed["total-perspective-vortex"])
	if parsed.get("zappy", {}):
		ai.append(parsed["zappy"])
	if parsed.get("lem_in", {}):
		ai.append(parsed["lem_in"])
	if parsed.get("corewar", {}):
		ai.append(parsed["corewar"])
	if parsed.get("Python for Data Science", {}):
		ai.append(parsed["Python for Data Science"])
	if parsed.get("Piscine Data Science", {}):
		ai.append(parsed["Piscine Data Science"])
	if parsed.get("Leaffliction", {}):
		ai.append(parsed["Leaffliction"])

	#Security 
	security = []
	if parsed.get("ft_nmap", {}):
		security.append(parsed["ft_nmap"])
	if parsed.get("snow-crash", {}):
		security.append(parsed["snow-crash"])
	if parsed.get("darkly", {}):
		security.append(parsed["darkly"])
	if parsed.get("rainfall", {}):
		security.append(parsed["rainfall"])
	if parsed.get("dr-quine", {}):
		security.append(parsed["dr-quine"])
	if parsed.get("woody-woodpacker", {}):
		security.append(parsed["woody-woodpacker"])
	if parsed.get("famine", {}):
		security.append(parsed["famine"])
	if parsed.get("pestilence", {}):
		security.append(parsed["pestilence"])
	if parsed.get("war", {}):
		security.append(parsed["war"])
	if parsed.get("death", {}):
		security.append(parsed["death"])
	if parsed.get("boot2root", {}):
		security.append(parsed["boot2root"])
	if parsed.get("ft_shield", {}):
		security.append(parsed["ft_shield"])
	if parsed.get("override", {}):
		security.append(parsed["override"])
	if parsed.get("ft_malcolm", {}):
		security.append(parsed["ft_malcolm"])
	if parsed.get("tinky-winkey", {}):
		security.append(parsed["tinky-winkey"])
	if parsed.get("Cybersecurity", {}):
		security.append(parsed["Cybersecurity"])

	# Networking
	devops = []
	if parsed.get("taskmaster", {}):
		devops.append(parsed["taskmaster"])
	if parsed.get("ft_ping", {}):
		devops.append(parsed["ft_ping"])
	if parsed.get("ft_traceroute", {}):
		devops.append(parsed["ft_traceroute"])
	if parsed.get("cloud-1", {}):
		devops.append(parsed["cloud-1"])
	if parsed.get("Inception-of-Things", {}):
		devops.append(parsed["Inception-of-Things"])
	if parsed.get("Bgp At Doors of Autonomous Systems is Simple", {}):
		devops.append(parsed["Bgp At Doors of Autonomous Systems is Simple"])

	# Web & Mobile
	web = []
	if parsed.get("ft_hangouts", {}):
		web.append(parsed["ft_hangouts"])
	if parsed.get("swifty-companion", {}):
		web.append(parsed["swifty-companion"])
	if parsed.get("camagru", {}):
		web.append(parsed["camagru"])
	if parsed.get("matcha", {}):
		web.append(parsed["matcha"])
	if parsed.get("hypertube", {}):
		web.append(parsed["hypertube"])
	if parsed.get("swifty-proteins", {}):
		web.append(parsed["swifty-proteins"])
	if parsed.get("music-room", {}):
		web.append(parsed["music-room"])
	if parsed.get("red-tetris", {}):
		web.append(parsed["red-tetris"])
	if parsed.get("Piscine RoR", {}):
		web.append(parsed["Piscine RoR"])
	if parsed.get("Piscine Django", {}):
		web.append(parsed["Piscine Django"])
	if parsed.get("Piscine Symfony", {}):
		web.append(parsed["Piscine Symfony"])
	if parsed.get("Mobile", {}):
		web.append(parsed["Mobile"])

	# Kernel
	kernel = []
	if parsed.get("libasm", {}):
		kernel.append(parsed["libasm"])
	if parsed.get("nibbler", {}):
		kernel.append(parsed["nibbler"])
	if parsed.get("strace", {}):
		kernel.append(parsed["strace"])
	if parsed.get("ft_linux", {}):
		kernel.append(parsed["ft_linux"])
	if parsed.get("little-penguin-1", {}):
		kernel.append(parsed["little-penguin-1"])
	if parsed.get("matt-daemon", {}):
		kernel.append(parsed["matt-daemon"])
	if parsed.get("process-and-memory", {}):
		kernel.append(parsed["process-and-memory"])
	if parsed.get("drivers-and-interrupts", {}):
		kernel.append(parsed["drivers-and-interrupts"])
	if parsed.get("filesystem", {}):
		kernel.append(parsed["filesystem"])
	if parsed.get("kfs-2", {}):
		kernel.append(parsed["kfs-2"])
	if parsed.get("kfs-1", {}):
		kernel.append(parsed["kfs-1"])
	if parsed.get("kfs-3", {}):
		kernel.append(parsed["kfs-3"])
	if parsed.get("kfs-4", {}):
		kernel.append(parsed["kfs-4"])
	if parsed.get("kfs-5", {}):
		kernel.append(parsed["kfs-5"])
	if parsed.get("kfs-6", {}):
		kernel.append(parsed["kfs-6"])
	if parsed.get("kfs-7", {}):
		kernel.append(parsed["kfs-7"])
	if parsed.get("kfs-8", {}):
		kernel.append(parsed["kfs-8"])
	if parsed.get("kfs-9", {}):
		kernel.append(parsed["kfs-9"])
	if parsed.get("kfs-x", {}):
		kernel.append(parsed["kfs-x"])
	if parsed.get("userspace_digressions", {}):
		kernel.append(parsed["userspace_digressions"])
	if parsed.get("lem-ipc", {}):
		kernel.append(parsed["lem-ipc"])
	if parsed.get("nm", {}):
		kernel.append(parsed["nm"])
	if parsed.get("malloc", {}):
		kernel.append(parsed["malloc"])
	if parsed.get("ft_ls", {}):
		kernel.append(parsed["ft_ls"])
	if parsed.get("42sh", {}):
		kernel.append(parsed["42sh"])

	# Graphics
	graphics = []
	if parsed.get("42run", {}):
		graphics.append(parsed["42run"])
	if parsed.get("bomberman", {}):
		graphics.append(parsed["bomberman"])
	if parsed.get("scop", {}):
		graphics.append(parsed["scop"])
	if parsed.get("humangl", {}):
		graphics.append(parsed["humangl"])
	if parsed.get("xv", {}):
		graphics.append(parsed["xv"])
	if parsed.get("in-the-shadows", {}):
		graphics.append(parsed["in-the-shadows"])
	if parsed.get("particle-system", {}):
		graphics.append(parsed["particle-system"])
	if parsed.get("ft_vox", {}):
		graphics.append(parsed["ft_vox"])
	if parsed.get("shaderpixel", {}):
		graphics.append(parsed["shaderpixel"])
	if parsed.get("guimp", {}):
		graphics.append(parsed["guimp"])
	if parsed.get("doom-nukem", {}):
		graphics.append(parsed["doom-nukem"])
	if parsed.get("mod1", {}):
		graphics.append(parsed["mod1"])
	if parsed.get("rt", {}):
		graphics.append(parsed["rt"])
	if parsed.get("ft_newton", {}):
		graphics.append(parsed["ft_newton"])
	if parsed.get("ft_minecraft", {}):
		graphics.append(parsed["ft_minecraft"])
	if parsed.get("Unity", {}):
		graphics.append(parsed["Unity"])

	# Crypto
	crypto = []
	if parsed.get("computorv1", {}):
		crypto.append(parsed["computorv1"])
	if parsed.get("computorv2", {}):
		crypto.append(parsed["computorv2"])
	if parsed.get("ft_ssl_rsa", {}):
		crypto.append(parsed["ft_ssl_rsa"])
	if parsed.get("ft_ssl_md5", {}):
		crypto.append(parsed["ft_ssl_md5"])
	if parsed.get("ft_ssl_des", {}):
		crypto.append(parsed["ft_ssl_des"])
	if parsed.get("ready set boole", {}):
		crypto.append(parsed["ready set boole"])
	if parsed.get("matrix", {}):
		crypto.append(parsed["matrix"])
	if parsed.get("ft_kalman", {}):
		crypto.append(parsed["ft_kalman"])


	# Dev
	dev = []
	if parsed.get("ft_turing", {}):
		dev.append(parsed["ft_turing"])
	if parsed.get("ft_ality", {}):
		dev.append(parsed["ft_ality"])
	if parsed.get("h42n42", {}):
		dev.append(parsed["h42n42"])
	if parsed.get("avaj-launcher", {}):
		dev.append(parsed["avaj-launcher"])
	if parsed.get("swingy", {}):
		dev.append(parsed["swingy"])
	if parsed.get("fix-me", {}):
		dev.append(parsed["fix-me"])
	if parsed.get("Open Project", {}):
		dev.append(parsed["Open Project"])
	if parsed.get("Rushes", {}):
		dev.append(parsed["Rushes"])
	if parsed.get("Piscine Object", {}):
		dev.append(parsed["Piscine Object"])
	if parsed.get("Abstract_data", {}):
		dev.append(parsed["Abstract_data"])
	if parsed.get("ft_lex", {}):
		dev.append(parsed["ft_lex"])
	if parsed.get("ft_yacc", {}):
		dev.append(parsed["ft_yacc"])





	# Load the LaTeX template
	with open("./src/transcript_template.tex") as f:
		template = Template(f.read())

	extra_vars = {
		"school_address": school_address,
		"first_name": first_name,
		"last_name": last_name,
		"date_of_birth": date_of_birth,
		"date_issued": date_issued,
		"passed_selection": passed_selection,
		"core_started": core_started,
		"core_completed": core_completed,
		"advanced_completed": advanced_completed,
		"rank0": rank0,
		"rank1": rank1,
		"rank2": rank2,
		"rank3": rank3,
		"rank4": rank4,
		"rank5": rank5,
		"rank6": rank6,
		"ai": ai,
		"security": security,
		"devops": devops,
		"web": web,
		"kernel": kernel,
		"graphics": graphics,
		"crypto": crypto,
		"dev": dev,

	}
	
	# Render the template with the JSON data
	output_tex = template.render(**extra_vars)

	# Save output .tex file
	with open("./data/output.tex", "w") as f:
		f.write(output_tex)
