class ControllerA(object):
    @staticmethod
    def to_dict(eps):
        eps_dict = {}
        eps_dict['MPPT_X.SOL_VOLT'] = eps.MPPT_X.SOL_VOLT
        eps_dict['MPPT_X.SOL_CURR'] = eps.MPPT_X.SOL_CURR
        eps_dict['MPPT_X.SOL_OUT_VOLT'] = eps.MPPT_X.SOL_OUT_VOLT
        eps_dict['MPPT_X.TEMP'] = eps.MPPT_X.TEMP
        eps_dict['MPPT_X.STATE'] = eps.MPPT_X.STATE

        eps_dict['MPPT_Y_PLUS.SOL_VOLT'] = eps.MPPT_Y_PLUS.SOL_VOLT
        eps_dict['MPPT_Y_PLUS.SOL_CURR'] = eps.MPPT_Y_PLUS.SOL_CURR
        eps_dict['MPPT_Y_PLUS.SOL_OUT_VOLT'] = eps.MPPT_Y_PLUS.SOL_OUT_VOLT
        eps_dict['MPPT_Y_PLUS.TEMP'] = eps.MPPT_Y_PLUS.TEMP
        eps_dict['MPPT_Y_PLUS.STATE'] = eps.MPPT_Y_PLUS.STATE

        eps_dict['MPPT_Y_MINUS.SOL_VOLT'] = eps.MPPT_Y_MINUS.SOL_VOLT
        eps_dict['MPPT_Y_MINUS.SOL_CURR'] = eps.MPPT_Y_MINUS.SOL_CURR
        eps_dict['MPPT_Y_MINUS.SOL_OUT_VOLT'] = eps.MPPT_Y_MINUS.SOL_OUT_VOLT
        eps_dict['MPPT_Y_MINUS.TEMP'] = eps.MPPT_Y_MINUS.TEMP
        eps_dict['MPPT_Y_MINUS.STATE'] = eps.MPPT_Y_MINUS.STATE

        eps_dict['DISTR.VOLT_3V3'] = eps.DISTR.VOLT_3V3
        eps_dict['DISTR.CURR_3V3'] = eps.DISTR.CURR_3V3
        eps_dict['DISTR.VOLT_5V'] = eps.DISTR.VOLT_5V
        eps_dict['DISTR.CURR_5V'] = eps.DISTR.CURR_5V
        eps_dict['DISTR.VOLT_VBAT'] = eps.DISTR.VOLT_VBAT
        eps_dict['DISTR.CURR_VBAT'] = eps.DISTR.CURR_VBAT
        eps_dict['DISTR.LCL_STATE'] = eps.DISTR.LCL_STATE
        eps_dict['DISTR.LCL_FLAGB'] = eps.DISTR.LCL_FLAGB

        eps_dict['BATC.VOLT_A'] = eps.BATC.VOLT_A
        eps_dict['BATC.CHRG_CURR'] = eps.BATC.CHRG_CURR
        eps_dict['BATC.DCHRG_CURR'] = eps.BATC.DCHRG_CURR
        eps_dict['BATC.TEMP'] = eps.BATC.TEMP
        eps_dict['BATC.STATE'] = eps.BATC.STATE

        eps_dict['BP.TEMP_A'] = eps.BP.TEMP_A
        eps_dict['BP.TEMP_B'] = eps.BP.TEMP_B

        eps_dict['CTRLB.VOLT_3V3d'] = eps.CTRLB.VOLT_3V3d

        eps_dict['CTRLA.SAFETY_CTR'] = eps.CTRLA.SAFETY_CTR
        eps_dict['CTRLA.PWR_CYCLES'] = eps.CTRLA.PWR_CYCLES
        eps_dict['CTRLA.UPTIME'] = eps.CTRLA.UPTIME
        eps_dict['CTRLA.TEMP'] = eps.CTRLA.TEMP
        eps_dict['CTRLA.SUPP_TEMP'] = eps.CTRLA.SUPP_TEMP

        eps_dict['DCDC3V3.TEMP'] = eps.DCDC3V3.TEMP
        eps_dict['DCDC5V.TEMP'] = eps.DCDC5V.TEMP

        return eps_dict


class ControllerB(object):
    @staticmethod
    def to_dict(eps):
        eps_dict = {}
        eps_dict['BP.TEMP_C'] = eps.BP.TEMP_C
        
        eps_dict['BATC.VOLT_B'] = eps.BATC.VOLT_B

        eps_dict['CTRLB.SAFETY_CTR'] = eps.CTRLB.SAFETY_CTR
        eps_dict['CTRLB.PWR_CYCLES'] = eps.CTRLB.PWR_CYCLES
        eps_dict['CTRLB.UPTIME'] = eps.CTRLB.UPTIME
        eps_dict['CTRLB.TEMP'] = eps.CTRLB.TEMP
        eps_dict['CTRLB.SUPP_TEMP'] = eps.CTRLB.SUPP_TEMP

        eps_dict['CTRLA.VOLT_3V3d'] = eps.CTRLA.VOLT_3V3d

        return eps_dict
