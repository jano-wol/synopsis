<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link :to="{ name: 'synopsis' }" :class="$route.name == 'synopsis' ? 'active' : ''"
                            class="nav-link" aria-current="page" href="#">Szinopszis
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{ name: 'index' }" :class="$route.name == 'index' ? 'active' : ''"
                            class="nav-link" aria-current="page" href="#">Tartalomjegyzék
                        </router-link>
                    </li>
                    <!-- <li class="nav-item">
                        <a class="nav-link" href="#">Fejlesztőknek</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Részletek</a>
                    </li> -->
                </ul>
            </div>
        </div>
    </nav>
</template>
