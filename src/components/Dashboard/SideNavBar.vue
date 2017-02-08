<template>
    <div>
        <nav class='sidenav white'>
            <ul class="sideul">
                <li>
                    <i class="fa fa-weixin white" aria-hidden="true"></i> Visitor
                </li>
                <VisitorList />
               
                <!--   <li>
                    <a href='#' class="white">
                        <i class="fa fa-cog white" aria-hidden="true"></i> Setting
                    </a>
                </li>
                <li id='re'>
                    <a href='#' class="white">
                        <i class="fa fa-cog white" aria-hidden="true"></i> Request
                    </a>
                </li> -->
            </ul>
        </nav>
        <!-- <div class="maincontent">
            <p>admin</p>
            name
            <input id='r' type="text" name="">
            <input id='join' type="button" value='join'>
            <br>
            <br> msg
            <input id='msg' type="text" name="">
            <input id='send' type="button" value='send'>
            <br>
            <p>users</p>
            <br>
            <ul id='users'></ul>
            <br>
            <p>msgs</p>
            <ul id='msgs'></ul>
        </div> -->
    </div>
</template>
<script>
import VisitorList from './VisitorList.vue'
export default {
    components:{
        VisitorList
    }
}
</script>
<style>
.sidenav {
    width: 200px;
    height: 100%;
    background-color: #012C32;
    position: fixed;
    left: 0px;
    top: 0px;
    text-align: center;
}

.white {
    color: #fff
}

.sidenav ul,
.sidenav li {
    list-style: none;
    padding: 0px;
    margin: 0px;
    line-height: 35px;
    cursor: pointer;
}

.sidenav li:hover {
    background-color: #00d1b2;
}

.maincontent {
    margin-left: 200px
}

.visitor-ul{
    background-color: #333333;
}

.or {
    background-color: #FFDB4A;
}
</style>
