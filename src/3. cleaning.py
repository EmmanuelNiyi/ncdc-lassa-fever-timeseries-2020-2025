# Standard library imports
import os
import re
import datetime as dt
import shutil
from urllib.parse import urljoin

# Third-party libraries
import requests
import pdfplumber
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from fpdf import FPDF
from typing import Optional, Dict, Any, Tuple



