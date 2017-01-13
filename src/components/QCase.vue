<template>
    <transition name="modal">
        <div class="modal-mask" @click="$emit('close')">
            <div class="modal-wrapper">
                <div class="modal-container" @click="preventClose">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <span>170 user(s) in waiting, 1 user(s) away from keyboard,</span>
                        </div>
                        <div class="panel-heading white-panel-head">
                            <input type="text" class="form-control" placeholder="global search...">
                        </div>
                        <div class="panel-body">
                            <div class="row">
                                <div class="col-sm-6 text-center" v-for="qcase in this.$store.state.qcases">
                                    <div class="case">
                                        <h3>
                                           {{ qcase.issue[0].content.desc }}
                                         </h3>
                                        <img class="qpic" :src="qcase.imgurl" />
                                        <ul class="qu">
                                            <li>
                                                <span>
                                             Token: {{ qcase.token }}
                                            </span>
                                            </li>
                                            <li>
                                                <span>
                                             Email: {{ qcase.email }}
                                            </span>
                                            </li>
                                            <li>
                                                <span>
                                            Phone: {{ qcase.phone }}
                                          </span>
                                            </li>
                                            <li>
                                                <span>
                                              Birthday : {{ qcase.birthday }}
                                            </span>
                                            </li>
                                            <li>
                                                <span>
                                              Country : {{ qcase.country }}
                                            </span>
                                            </li>
                                            <li>
                                                <span>
                                              RequestDate:{{casePassedTime(qcase.issue[0].reporttime)}}
                                            </span>
                                            </li>
                                        </ul>
                                    </div>
                                    <br />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </transition>
</template>
<script>
export default {
    created() {
            window.setInterval(() => {
                this.now = new Date()
            }, 1000);
            console.log(this.now)
        },
        data() {
            return {
                now: new Date()
            }
        },
        methods: {
            g: function(url){
                
                return  "../../../../" + url
            },
            casePassedTime: function(time) {
                var caseTime = new Date(time * 1000)
                var timediff = new Date(this.now - caseTime) / 1000
                return Math.trunc(timediff %60)
                //return timediff
            },
            preventClose: function(e) {
                e.stopPropagation();
                //e.preventDefault();
            }
        }
}
</script>
<style>
.qu {
    margin-top: 10px;
    text-align: left;
}

.qpic {
    width: 250px;
    margin-left: auto;
    margin-right: auto;
    padding: 4px;
    border: 1px solid #ddd;
}

.case {
    border: 1px solid #ddd;
    padding: 5px;
}

.white-panel-head {
    background-color: #fff !important
}

.modal-mask {
    position: fixed;
    z-index: 99999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: table;
    transition: opacity .3s ease;
}

.modal-wrapper {
    display: table-cell;
    vertical-align: middle;
}

.modal-container {
    width: 80%;
    height: 80%;
    margin: 0px auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
    transition: all .3s ease;
    font-family: Helvetica, Arial, sans-serif;
    overflow: scroll;
    overflow-x: hidden;
}

.modal-header h3 {
    margin-top: 0;
    color: #42b983;
}

.modal-body {
    margin: 20px 0;
    overflow: scroll;
}

.modal-default-button {
    float: right;
}


/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
    opacity: 0;
}

.modal-leave-active {
    opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
}
</style>
