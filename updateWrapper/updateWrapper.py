from elasticsearch import Elasticsearch

__author__ = "Sebastian Schüpbach"
__copyright__ = "Copyright 2016, swissbib project, UB Basel"
__license__ = "http://opensource.org/licenses/gpl-2.0.php"
__version__ = "0.1"
__maintainer__ = "Sebastian Schüpbach"
__email__ = "sebastian.schuepbach@unibas.ch"
__status__ = "development"

"""
1. Send bulkDelete file to Elasticsearch
2. Kick off Metafacture / enrichment workflow
3. Initialise Spark workflow
"""

bulk = Elasticsearch.bulk
