import http.client

conn = http.client.HTTPSConnection("services.chanel.com")

payload = "division%5B%5D=1&division%5B%5D=2&division%5B%5D=5&division%5B%5D=3&productline%5B%5D=1&productline%5B%5D=2&productline%5B%5D=3&productline%5B%5D=4&productline%5B%5D=26&productline%5B%5D=5&productline%5B%5D=18&productline%5B%5D=19&productline%5B%5D=25&productline%5B%5D=10&productline%5B%5D=14&productline%5B%5D=13&productline%5B%5D=12&chanel-only=1&geocodeResults=%5B%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%2225%22%2C%22short_name%22%3A%2225%22%2C%22types%22%3A%5B%22street_number%22%5D%7D%2C%7B%22long_name%22%3A%22Ulitsa%20Zamoronova%22%2C%22short_name%22%3A%22Ulitsa%20Zamoronova%22%2C%22types%22%3A%5B%22route%22%5D%7D%2C%7B%22long_name%22%3A%22Tsentralnyy%20administrativnyy%20okrug%22%2C%22short_name%22%3A%22Tsentralnyy%20administrativnyy%20okrug%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Presnenskiy%22%2C%22short_name%22%3A%22Presnenskiy%22%2C%22types%22%3A%5B%22administrative_area_level_3%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22123022%22%2C%22short_name%22%3A%22123022%22%2C%22types%22%3A%5B%22postal_code%22%5D%7D%5D%2C%22formatted_address%22%3A%22Ulitsa%20Zamoronova%2C%2025%2C%20Moskva%2C%20Russia%2C%20123022%22%2C%22geometry%22%3A%7B%22location%22%3A%7B%22lat%22%3A55.7604409%2C%22lng%22%3A37.5687909%7D%2C%22location_type%22%3A%22ROOFTOP%22%2C%22viewport%22%3A%7B%22south%22%3A55.7590919197085%2C%22west%22%3A37.5674419197085%2C%22north%22%3A55.7617898802915%2C%22east%22%3A37.57013988029149%7D%7D%2C%22place_id%22%3A%22ChIJD1vuujJKtUYR6GNVPBWiukk%22%2C%22plus_code%22%3A%7B%22compound_code%22%3A%22QH69%2B5G%20Presnensky%20District%2C%20Moscow%2C%20Russia%22%2C%22global_code%22%3A%229G7VQH69%2B5G%22%7D%2C%22types%22%3A%5B%22street_address%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%2224%20%D1%81%D1%82%D1%80%D0%BE%D0%B5%D0%BD%D0%B8%D0%B5%203%22%2C%22short_name%22%3A%2224%20%D1%81%D1%82%D1%80%D0%BE%D0%B5%D0%BD%D0%B8%D0%B5%203%22%2C%22types%22%3A%5B%22street_number%22%5D%7D%2C%7B%22long_name%22%3A%22Ulitsa%20Zamoronova%22%2C%22short_name%22%3A%22Ulitsa%20Zamoronova%22%2C%22types%22%3A%5B%22route%22%5D%7D%2C%7B%22long_name%22%3A%22Tsentralnyy%20administrativnyy%20okrug%22%2C%22short_name%22%3A%22Tsentralnyy%20administrativnyy%20okrug%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Presnenskiy%22%2C%22short_name%22%3A%22Presnenskiy%22%2C%22types%22%3A%5B%22administrative_area_level_3%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22123022%22%2C%22short_name%22%3A%22123022%22%2C%22types%22%3A%5B%22postal_code%22%5D%7D%5D%2C%22formatted_address%22%3A%22Ulitsa%20Zamoronova%2C%2024%20%D1%81%D1%82%D1%80%D0%BE%D0%B5%D0%BD%D0%B8%D0%B5%203%2C%20Moskva%2C%20Russia%2C%20123022%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.7607419%2C%22west%22%3A37.5692248%2C%22north%22%3A55.7611329%2C%22east%22%3A37.5697147%7D%2C%22location%22%3A%7B%22lat%22%3A55.7609402%2C%22lng%22%3A37.5694857%7D%2C%22location_type%22%3A%22ROOFTOP%22%2C%22viewport%22%3A%7B%22south%22%3A55.7595884197085%2C%22west%22%3A37.5681207697085%2C%22north%22%3A55.7622863802915%2C%22east%22%3A37.5708187302915%7D%7D%2C%22place_id%22%3A%22ChIJT8LulzJKtUYRX_nr3PAG4v0%22%2C%22types%22%3A%5B%22premise%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%2225%2F5%22%2C%22short_name%22%3A%2225%2F5%22%2C%22types%22%3A%5B%22street_number%22%5D%7D%2C%7B%22long_name%22%3A%22Ulitsa%20Zamoronova%22%2C%22short_name%22%3A%22Ulitsa%20Zamoronova%22%2C%22types%22%3A%5B%22route%22%5D%7D%2C%7B%22long_name%22%3A%22Tsentralnyy%20administrativnyy%20okrug%22%2C%22short_name%22%3A%22Tsentralnyy%20administrativnyy%20okrug%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Presnenskiy%22%2C%22short_name%22%3A%22Presnenskiy%22%2C%22types%22%3A%5B%22administrative_area_level_3%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22123022%22%2C%22short_name%22%3A%22123022%22%2C%22types%22%3A%5B%22postal_code%22%5D%7D%5D%2C%22formatted_address%22%3A%22Ulitsa%20Zamoronova%2C%2025%2F5%2C%20Moskva%2C%20Russia%2C%20123022%22%2C%22geometry%22%3A%7B%22location%22%3A%7B%22lat%22%3A55.7604409%2C%22lng%22%3A37.5687909%7D%2C%22location_type%22%3A%22ROOFTOP%22%2C%22viewport%22%3A%7B%22south%22%3A55.7590919197085%2C%22west%22%3A37.5674419197085%2C%22north%22%3A55.7617898802915%2C%22east%22%3A37.57013988029149%7D%7D%2C%22place_id%22%3A%22ChIJsZ3YF-FLtUYRigJ6DvLiOQA%22%2C%22plus_code%22%3A%7B%22compound_code%22%3A%22QH69%2B5G%20Presnensky%20District%2C%20Moscow%2C%20Russia%22%2C%22global_code%22%3A%229G7VQH69%2B5G%22%7D%2C%22types%22%3A%5B%22establishment%22%2C%22health%22%2C%22pharmacy%22%2C%22point_of_interest%22%2C%22store%22%2C%22veterinary_care%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%2225%22%2C%22short_name%22%3A%2225%22%2C%22types%22%3A%5B%22street_number%22%5D%7D%2C%7B%22long_name%22%3A%22Ulitsa%20Zamoronova%22%2C%22short_name%22%3A%22Ulitsa%20Zamoronova%22%2C%22types%22%3A%5B%22route%22%5D%7D%2C%7B%22long_name%22%3A%22Tsentralnyy%20administrativnyy%20okrug%22%2C%22short_name%22%3A%22Tsentralnyy%20administrativnyy%20okrug%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Presnenskiy%22%2C%22short_name%22%3A%22Presnenskiy%22%2C%22types%22%3A%5B%22administrative_area_level_3%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22123022%22%2C%22short_name%22%3A%22123022%22%2C%22types%22%3A%5B%22postal_code%22%5D%7D%5D%2C%22formatted_address%22%3A%22Ulitsa%20Zamoronova%2C%2025%2C%20Moskva%2C%20Russia%2C%20123022%22%2C%22geometry%22%3A%7B%22location%22%3A%7B%22lat%22%3A55.760737%2C%22lng%22%3A37.5688289%7D%2C%22location_type%22%3A%22RANGE_INTERPOLATED%22%2C%22viewport%22%3A%7B%22south%22%3A55.7593880197085%2C%22west%22%3A37.5674799197085%2C%22north%22%3A55.76208598029149%2C%22east%22%3A37.5701778802915%7D%7D%2C%22place_id%22%3A%22Ei1VbGl0c2EgWmFtb3Jvbm92YSwgMjUsIE1vc2t2YSwgUnVzc2lhLCAxMjMwMjIiGhIYChQKEgn36k6jMkq1RhEFy050GaBA8xAZ%22%2C%22types%22%3A%5B%22street_address%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22QH69%2B9H%22%2C%22short_name%22%3A%22QH69%2B9H%22%2C%22types%22%3A%5B%22plus_code%22%5D%7D%2C%7B%22long_name%22%3A%22Central%20Administrative%20Okrug%22%2C%22short_name%22%3A%22Central%20Administrative%20Okrug%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Presnenskiy%22%2C%22short_name%22%3A%22Presnenskiy%22%2C%22types%22%3A%5B%22administrative_area_level_3%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22QH69%2B9H%20Presnensky%20District%2C%20Moscow%2C%20Russia%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.760875%2C%22west%22%3A37.56887500000001%2C%22north%22%3A55.761%2C%22east%22%3A37.569%7D%2C%22location%22%3A%7B%22lat%22%3A55.7609654%2C%22lng%22%3A37.5688916%7D%2C%22location_type%22%3A%22GEOMETRIC_CENTER%22%2C%22viewport%22%3A%7B%22south%22%3A55.7595885197085%2C%22west%22%3A37.5675885197085%2C%22north%22%3A55.76228648029149%2C%22east%22%3A37.5702864802915%7D%7D%2C%22place_id%22%3A%22GhIJmzFxUGfhS0ARDHygcNHIQkA%22%2C%22plus_code%22%3A%7B%22compound_code%22%3A%22QH69%2B9H%20Presnensky%20District%2C%20Moscow%2C%20Russia%22%2C%22global_code%22%3A%229G7VQH69%2B9H%22%7D%2C%22types%22%3A%5B%22plus_code%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%2225%22%2C%22short_name%22%3A%2225%22%2C%22types%22%3A%5B%22street_number%22%5D%7D%2C%7B%22long_name%22%3A%22Ulitsa%20Zamoronova%22%2C%22short_name%22%3A%22Ulitsa%20Zamoronova%22%2C%22types%22%3A%5B%22route%22%5D%7D%2C%7B%22long_name%22%3A%22Tsentralnyy%20administrativnyy%20okrug%22%2C%22short_name%22%3A%22Tsentralnyy%20administrativnyy%20okrug%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Presnenskiy%22%2C%22short_name%22%3A%22Presnenskiy%22%2C%22types%22%3A%5B%22administrative_area_level_3%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moskva%22%2C%22short_name%22%3A%22Moskva%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22123022%22%2C%22short_name%22%3A%22123022%22%2C%22types%22%3A%5B%22postal_code%22%5D%7D%5D%2C%22formatted_address%22%3A%22Ulitsa%20Zamoronova%2C%2025%2C%20Moskva%2C%20Russia%2C%20123022%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.760737%2C%22west%22%3A37.5685173%2C%22north%22%3A55.7608173%2C%22east%22%3A37.5688289%7D%2C%22location%22%3A%7B%22lat%22%3A55.7607772%2C%22lng%22%3A37.5686731%7D%2C%22location_type%22%3A%22GEOMETRIC_CENTER%22%2C%22viewport%22%3A%7B%22south%22%3A55.7594281697085%2C%22west%22%3A37.56732411970849%2C%22north%22%3A55.76212613029149%2C%22east%22%3A37.57002208029149%7D%7D%2C%22place_id%22%3A%22ChIJ83qBozJKtUYRjBD46PyXOt4%22%2C%22types%22%3A%5B%22route%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22123022%22%2C%22short_name%22%3A%22123022%22%2C%22types%22%3A%5B%22postal_code%22%5D%7D%2C%7B%22long_name%22%3A%22Central%20Administrative%20Okrug%22%2C%22short_name%22%3A%22Central%20Administrative%20Okrug%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Presnenskiy%22%2C%22short_name%22%3A%22Presnenskiy%22%2C%22types%22%3A%5B%22administrative_area_level_3%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Moscow%2C%20Russia%2C%20123022%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.752841%2C%22west%22%3A37.547393%2C%22north%22%3A55.773977%2C%22east%22%3A37.571741%7D%2C%22location%22%3A%7B%22lat%22%3A55.7663838%2C%22lng%22%3A37.5540539%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A55.752841%2C%22west%22%3A37.547393%2C%22north%22%3A55.773977%2C%22east%22%3A37.571741%7D%7D%2C%22place_id%22%3A%22ChIJsYm8QodJtUYR2vOuo6myO0Y%22%2C%22types%22%3A%5B%22postal_code%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22Presnensky%20District%22%2C%22short_name%22%3A%22Presnensky%20District%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_2%22%5D%7D%2C%7B%22long_name%22%3A%22Central%20Administrative%20Okrug%22%2C%22short_name%22%3A%22Central%20Administrative%20Okrug%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Presnenskiy%22%2C%22short_name%22%3A%22Presnenskiy%22%2C%22types%22%3A%5B%22administrative_area_level_3%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Presnensky%20District%2C%20Moscow%2C%20Russia%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.7445831%2C%22west%22%3A37.514144%2C%22north%22%3A55.775913%2C%22east%22%3A37.609413%7D%2C%22location%22%3A%7B%22lat%22%3A55.763347%2C%22lng%22%3A37.5606519%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A55.7445831%2C%22west%22%3A37.514144%2C%22north%22%3A55.775913%2C%22east%22%3A37.609413%7D%7D%2C%22place_id%22%3A%22ChIJFzGu6dJLtUYR1DTn_R7_Ioc%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_2%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22Presnenskiy%22%2C%22short_name%22%3A%22Presnenskiy%22%2C%22types%22%3A%5B%22administrative_area_level_3%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Central%20Administrative%20Okrug%22%2C%22short_name%22%3A%22Central%20Administrative%20Okrug%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Presnenskiy%2C%20Moscow%2C%20Russia%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.7444889%2C%22west%22%3A37.514311%2C%22north%22%3A55.77585699999999%2C%22east%22%3A37.6098178%7D%2C%22location%22%3A%7B%22lat%22%3A55.7630691%2C%22lng%22%3A37.5629076%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A55.7444889%2C%22west%22%3A37.514311%2C%22north%22%3A55.77585699999999%2C%22east%22%3A37.6098178%7D%7D%2C%22place_id%22%3A%22ChIJyWdgxNJLtUYRvpMuxoPm-LU%22%2C%22types%22%3A%5B%22administrative_area_level_3%22%2C%22political%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22Central%20Administrative%20Okrug%22%2C%22short_name%22%3A%22Central%20Administrative%20Okrug%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Central%20Administrative%20Okrug%2C%20Moscow%2C%20Russia%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.710244%2C%22west%22%3A37.514274%2C%22north%22%3A55.797092%2C%22east%22%3A37.7135712%7D%2C%22location%22%3A%7B%22lat%22%3A55.7569428%2C%22lng%22%3A37.6149895%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A55.710244%2C%22west%22%3A37.514274%2C%22north%22%3A55.797092%2C%22east%22%3A37.7135712%7D%7D%2C%22place_id%22%3A%22ChIJz08vV1BKtUYR2D1lCclQxZM%22%2C%22types%22%3A%5B%22political%22%2C%22sublocality%22%2C%22sublocality_level_1%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Moscow%2C%20Russia%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.142591%2C%22west%22%3A36.8032249%2C%22north%22%3A56.0214609%2C%22east%22%3A37.9678221%7D%2C%22location%22%3A%7B%22lat%22%3A55.755826%2C%22lng%22%3A37.6172999%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A55.142591%2C%22west%22%3A36.8032249%2C%22north%22%3A56.0214609%2C%22east%22%3A37.9678221%7D%7D%2C%22place_id%22%3A%22ChIJybDUc_xKtUYRTM9XV8zWRD0%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Moscow%2C%20Russia%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.1428781%2C%22west%22%3A36.8037541%2C%22north%22%3A56.02156799999999%2C%22east%22%3A37.9678191%7D%2C%22location%22%3A%7B%22lat%22%3A55.5464948%2C%22lng%22%3A37.2926266%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A55.1428781%2C%22west%22%3A36.8037541%2C%22north%22%3A56.02156799999999%2C%22east%22%3A37.9678191%7D%7D%2C%22place_id%22%3A%22ChIJP5cfydBLtUYRyvGyUIpYc50%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Moscow%2C%20Russia%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.1428781%2C%22west%22%3A36.8037541%2C%22north%22%3A56.02156799999999%2C%22east%22%3A37.9678191%7D%2C%22location%22%3A%7B%22lat%22%3A55.5464948%2C%22lng%22%3A37.2926266%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A55.1428781%2C%22west%22%3A36.8037541%2C%22north%22%3A56.02156799999999%2C%22east%22%3A37.9678191%7D%7D%2C%22place_id%22%3A%22ChIJr-dYmSzISkERysTPiPSjVws%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22Russia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Russia%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A41.185353%2C%22west%22%3A19.6160999%2C%22north%22%3A82.1673907%2C%22east%22%3A-168.9729426%7D%2C%22location%22%3A%7B%22lat%22%3A61.52401%2C%22lng%22%3A105.318756%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A41.185353%2C%22west%22%3A19.6160999%2C%22north%22%3A82.1673907%2C%22east%22%3A-168.9729426%7D%7D%2C%22place_id%22%3A%22ChIJ-yRniZpWPEURE_YRZvj9CRQ%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D&radius=24.836363636363636"

headers = {
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    'X-Requested-With': "XMLHttpRequest"
    }

conn.request("POST", "/en_US/storelocator/getStoreList", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
