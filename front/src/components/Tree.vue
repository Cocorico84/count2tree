<template>
    <v-container>
        <v-layout v-if="tree !== null">
            <v-flex xs6>
                <v-card color="#C5E1A5"  class="mx-auto">
                    <v-card-title>{{ tree.genus }} {{ tree.specie }} {{ tree.variety }}</v-card-title>
                    <v-card-text>{{ tree.location }}</v-card-text>
                    <v-card-text>Hauteur : {{ tree.height }} m</v-card-text>
                    <v-col class="text-right">
                        <v-btn
                        text icon 
                        :color="color" 
                        @click="change_color"
                        >
                        <v-icon>mdi-heart</v-icon>
                        </v-btn>
                    </v-col>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        props: ['tree'],
        data: () => ({
            color : 'grey'
        }),
        methods: {
            change_color () {  
                this.color = "pink"            
            }
        }
    };
</script>/