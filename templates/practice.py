



<!--        -->
<!--        <td>-->
<!--            <div class="card mx-3 mt-4 shadow col d-flex justify-content-center bg-primary" style="width:200px;hight:20px">-->
<!--                <img src="/media/{{i.image}}" alt="Love" width="198px" height="200px">-->
<!--                <div class="cord-body mb-8">-->

<!--                    <p class="card-text"><h5>{{i.pname}}</h5></p>-->
<!--                    <h4 class="card-title">Rs.{{i.prize}}/kg.</h4>-->

<!--                    {% if i.id|is_in_cart:request.session.cart %}-->
<!--                    <div class="card-footer row no-gutters p-0">-->
<!--                        <table>-->
<!--                            <tr>-->
<!--                                <td>-->
<!--                                    <form action="" method="post">-->
<!--                                        {% csrf_token %}-->
<!--                                        <input hidden type="number" value="{{i.id}}" name="remove">-->
<!--                                        <input type="submit" value="-" class="col-5 btn btn-secondary active mx-3 no-gutters">-->
<!--                                    </form>-->
<!--                                </td>-->
<!--                                <td>-->
<!--                                    <div class="text-center col-10 mx-4">{{i.id|quantity:request.session.cart}}</div>-->
<!--                                </td>-->
<!--                                <td>-->
<!--                                    <form action="" method="post">-->
<!--                                        {% csrf_token %}-->
<!--                                        <input hidden type="number" value="{{i.id}}" name="add">-->
<!--                                        <input type="submit" value="+" class="col-8 btn btn-secondary active mx-30" style="font:italic">-->
<!--                                    </form>-->
<!--                                </td>-->
<!--                            </tr>-->

<!--                        </table>-->

<!--                    </div>-->

<!--                    {% else %}-->


<!--                    <form action="" method="post">-->
<!--                        {% csrf_token %}-->
<!--                        <input hidden type="number" value="{{i.id}}" name="pid">-->
<!--                        <input type="submit" value="Add to cart" class="btn btn-success border col-sm-10 mx-3 md-4">-->
<!--                        {% endif %}-->
<!--                    </form>-->
<!--                     <a href="/order/{{i.id}}"class="btn btn-success border col-sm-10 mx-3 md-4">Place Order</a>-->


<!--                    <br>-->
<!--                    <br>-->

<!--                </div>-->
<!--            </div>-->
<!--        </td>-->
<!--    </div>-->
<!--</table>-->
<!--<h3>{{cart}}</h3>-->

<!--    <div class="row">-->
<!--        {% for i in data %}-->



<!--    </div>-->











