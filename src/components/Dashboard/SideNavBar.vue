<template>
    <div>
        <nav class='sidenav white'>
            <ul class="sideul">
                <li>
                    <i class="fa fa-weixin white" aria-hidden="true"></i> Visitor
                </li>
               
               
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

    </div>
</template>
<script>

export default {
    components:{
       
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

.visitor-ul{
    background-color: #333333;
}

.or {
    background-color: #FFDB4A;
}
</style>
