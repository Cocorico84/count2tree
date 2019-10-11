from flask import request
from flask_restful import Resource

from treeroot.managers.trees import search_trees , get_tree_by_genus, get_locations, get_height, get_tree_height_by_locations


class Trees(Resource):
    def get(self):
        query = request.args['query']
        trees_matching = search_trees(query)
        trees = [tree.get_small_data() for tree in trees_matching]
        return trees


class Tree(Resource):
    def get(self, genus):
        tree = get_tree_by_genus(genus)
        return tree.get_small_data()


class Location(Resource):
    def get(self):
        locations = get_locations()
        return locations


class Height(Resource):
    def get(self):
        location = request.args.get('query', None)
        if location is not None:
            height_by_locations = get_tree_height_by_locations(location)
            return height_by_locations

        height = get_height()
        return height