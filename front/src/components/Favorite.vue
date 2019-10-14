<template>
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> (no branch): Auto stash before checking out "Favorite"
                <v-card class="pa-2">
=======
=======
>>>>>>> Stashed changes
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
>>>>>>> (no branch): Auto stash before checking out "Favorite"
    <v-container>
        <v-layout>
            <v-flex xs8>
                <v-card max-width="475" class="pa-2">
<<<<<<< Updated upstream
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> (no branch): Auto stash before checking out "Favorite"
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
                    <v-toolbar color="teal" dark>
                        <v-toolbar-title>Favorites</v-toolbar-title>
                    <div class="flex-grow-1"></div>
                    <v-btn icon >
                        <v-icon>mdi-delete</v-icon>
                    </v-btn>
                    </v-toolbar>
                        <v-list>
                            <v-list-item-group
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
                                v-model="settings"
>>>>>>> Stashed changes
=======
                                v-model="settings"
>>>>>>> Stashed changes
>>>>>>> (no branch): Auto stash before checking out "Favorite"
=======
                                v-model="settings"
>>>>>>> Stashed changes
=======
                                v-model="settings"
>>>>>>> Stashed changes
                                multiple
                                active-class=""
                            >
                                <v-list-item>
                                <template v-slot:default="{ active }">
                                    <v-list-item-action>
                                    <v-checkbox v-model="active"></v-checkbox>
                                    </v-list-item-action>
                                    <v-list-item-content>
                                    <v-list-item-title>Notifications</v-list-item-title>
                                    </v-list-item-content>
                                </template>
                                </v-list-item>
                            </v-list-item-group>
                            </v-list>
                </v-card>
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< 76ae67f800a48c4ce857c593f96d528a0c2e1568
=======
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
            </v-flex>
        </v-layout>
    </v-container>
>>>>>>> Stashed changes
=======
            </v-flex>
        </v-layout>
    </v-container>
>>>>>>> Stashed changes
>>>>>>> (no branch): Auto stash before checking out "Favorite"
=======
            </v-flex>
        </v-layout>
    </v-container>
>>>>>>> Stashed changes
=======
            </v-flex>
        </v-layout>
    </v-container>
>>>>>>> Stashed changes
</template>

<script>
export default {
    data: () => ({
        selected : []
        }),

}
</script>

