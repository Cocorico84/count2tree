from flask import request
from flask_restful import Resource

from treeroot.managers.trees import search_trees , get_tree_by_genus, get_locations, get_height, create_user , get_tree_height_by_locations, add_favorite


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


class User(Resource):
    def post(self):
        data = request.json
        user = create_user(data['username'],data['password'])
        return user.get_data()


class Favorite(Resource):
    def post(self):
        data = request.json
        print(data)
        favorite = add_favorite(data['genus'],data['specie'],data['variety'])
        return favorite.data()