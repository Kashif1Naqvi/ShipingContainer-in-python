import iso6346

class ShipingContainer:

    HEIGHT_FT  = 8.5
    WIDTH_FT   = 8.0

    next_serial = 11

    # @staticmethod #  static method can be called without an object for that class
    # def _get_next_serial():
    #     result = ShipingContainer.next_serial
    #     ShipingContainer.next_serial +=1
    #     return result
    #with the use of classmethod
    @staticmethod
    def _make_bic_code(owner_code,serial):
        return iso6346.create(owner_code=owner_code,serial=str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial +=1
        return result

    @classmethod
    def create_empty(cls,owner_code,length_ft,*args,**kwargs):
        return cls(owner_code ,length_ft, contents = None ,*args,**kwargs )
    @classmethod  #bellow like a shiping container
    def create_with_items(cls,owner_code,length_ft,items,*args,**kwargs):
        return cls(owner_code ,length_ft, contents=list(items),*args,**kwargs)

    def __init__(self,owner_code,length_ft,contents):
        # self.owner_code = owner_code
        self.contents = contents
        self.length_ft = length_ft
        # self.serial   = ShipingContainer.next_serial
        # ShipingContainer.next_serial += 1
        # self.serial = ShipingContainer._get_next_serial()
        self.bic = self._make_bic_code(
            owner_code = owner_code,
            serial = ShipingContainer._get_next_serial()
        )
    def _calc_volumn(self):
        return ShipingContainer.HEIGHT_FT * ShipingContainer.WIDTH_FT * self.length_ft
    @property
    def volumn_ft3(self):
        return self._calc_volumn()


""" increment by one ShipingContainer.next_serial += 1 """

class RefrigeratedShippingContiner(ShipingContainer):
    MAX_CELSIUS = 4.0

    FRIDGE_VOLUMN_FT3 = 100

    @staticmethod
    def _make_bic_code(owner_code,serial):
        return iso6346.create(
            owner_code=owner_code,
            serial = str(serial).zfill(6),
            category = 'R')

    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    def _f_to_c(fahrenheit):
        return (fahrenheit - 32 ) * 5/9

    def __init__(self,owner_code,length_ft,contents,celsius):
        super().__init__(owner_code,length_ft,contents)
        # if celsius >    RefrigeratedShippingContiner.MAX_CELSIUS:
        #     raise ValueError("Temprature too Hot")
        # self.celsius = celsius # in this way the value of the function is change so we avoide to do
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    def _set_celsius(self,value):
        if value >  RefrigeratedShippingContiner.MAX_CELSIUS:
            raise ValueError("Temprature too hot")

    @celsius.setter
    def celsius(self,value):
        # if value > RefrigeratedShippingContiner.MAX_CELSIUS:
        #     raise ValueError("Temprature is too Hot!")
        # self._celsius = value
        self._set_celsius(value)


    @property
    def fahrenheit(self):
        return RefrigeratedShippingContiner._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self,value):
        self.celsius = RefrigeratedShippingContiner._f_to_c(value)

    # @property
    # def volumn_ft3(self):
    #     return super().volumn_ft3 - RefrigeratedShippingContiner.FRIDGE_VOLUMN_FT3
    # drived from super class

    def _calc_volumn(self):
        return super()._calc_volumn() - RefrigeratedShippingContiner.FRIDGE_VOLUMN_FT3

class HeatedRefrigeratedShippingContiner(RefrigeratedShippingContiner):
    MIN_CELSIUS = -20.0
    # @RefrigeratedShippingContiner.celsius.setter
    def _set_celsius(self,value):
        # if not (HeatedRefrigeratedShippingContiner.MIN_CELSIUS
        #         <= value
        #         <= RefrigeratedShippingContiner.MAX_CELSIUS):   #already created in super class
        #     raise ValueError("Temprature out of the range!")
        # self._celsius = value
        if value < HeatedRefrigeratedShippingContiner.MIN_CELSIUS:
            raise ValueError("Temprature too cold!")
        # RefrigeratedShippingContiner.celsius.fset(self, value)
        super()._set_celsius(value)
