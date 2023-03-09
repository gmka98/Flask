import functools
from flask import blueprints, request, render_template, session, url_for, redirect
from werkzeug.security import check_password_hash, generate_password_hash