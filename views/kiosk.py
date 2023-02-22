from flask import Blueprint, render_template, request, session, redirect, jsonify, send_file
from flask_session import Session
import os
import json

app = Blueprint("kiosk",__name__,template_folder='pages')

# rapid = mysql(c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE)
# rapid= sqlite("assets\\db\\dti_rapidxi.db")
# rapid= sqlite(c.SQLITE_DB)

class _main:
	def __init__(self, arg):
		super(_main, self).__init__()
		self.arg = arg

	@app.route("/",methods=["POST","GET"])
	def kiosk():
		# return render_template("SITE_OFF.html") # MAINTENANCE
		# return "hi"
		return render_template("kiosk_main.html", services_pdf = _main.list_services_pdf())


	def list_services_pdf():
		dir_path = "assets/pdf/"
		return os.listdir(dir_path)
		# for path in os.listdir(dir_path):


	@app.route("/pdf/<pdf_name>",methods=["POST","GET"])
	def pdf_returns(pdf_name):
		dir_path = "assets/pdf/"
		return send_file(dir_path+pdf_name)
		# return render_template("SITE_OFF.html") # MAINTENANCE
		# return "hi"